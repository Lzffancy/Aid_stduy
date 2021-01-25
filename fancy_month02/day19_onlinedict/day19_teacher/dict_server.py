"""
dict 服务端逻辑处理
"""
from socket import *
from multiprocessing import Process
from dict_db import *
from time import sleep


# 处理客户端具体请求
class Handle:
    def __init__(self, connfd):
        self.connfd = connfd

    def do_register(self, name, passwd):
        if db.register(name, passwd):
            self.connfd.send(b"OK")
        else:
            self.connfd.send(b"FAIL")

    def do_login(self, name, passwd):
        if db.login(name, passwd):
            self.connfd.send(b"OK")
        else:
            self.connfd.send(b"FAIL")

    def do_query(self, name, word):
        mean = db.query(word)
        self.connfd.send(mean.encode())
        db.insert_hist(name, word)

    def do_hist(self, name):
        # data--> ((name,word,time),())
        data = db.history(name)
        for row in data:
            msg = "%s    %s    %s" % row
            self.connfd.send(msg.encode())
            sleep(0.1)
        self.connfd.send(b"##")

    # 具体处理请求函数 （逻辑处理）
    def request(self):
        # 接收各种请求，分情况讨论
        while True:
            data = self.connfd.recv(1024).decode()
            tmp = data.split(" ")
            if not data or data == "E":
                return
            elif tmp[0] == 'R':
                # tmp-> [R,name,passwd]
                self.do_register(tmp[1], tmp[2])
            elif tmp[0] == 'L':
                # tmp-> [L,name,passwd]
                self.do_login(tmp[1], tmp[2])
            elif tmp[0] == 'Q':
                # tmp-> [Q,name,word]
                self.do_query(tmp[1], tmp[2])
            elif tmp[0] == 'H':
                # tmp-> [H,name]
                self.do_hist(tmp[1])


# 创建进程
class ProcessServer(Process):
    def __init__(self, connfd):
        self.connfd = connfd
        self.handle = Handle(connfd)
        super().__init__(daemon=True)

    def run(self):
        db.cursor()  # 每个进程都生成自己的游标
        self.handle.request()  # 处理请求
        db.cur.close()
        self.connfd.close()


# 网络搭建
class DictServer:
    """
    提供网络功能
    """

    def __init__(self, *, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self.__create_socket()

    def __create_socket(self):
        tcp_socket = socket()
        tcp_socket.bind(self.address)
        return tcp_socket

    # 启动服务 --> 准备连接客户端
    def serve_forever(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)

        while True:
            try:
                connfd, addr = self.sock.accept()
                print("Connect from", addr)
            except KeyboardInterrupt:
                db.close()
                self.sock.close()
                return
            # 创建进程
            p = ProcessServer(connfd)
            p.start()


if __name__ == '__main__':
    dict = DictServer(host="0.0.0.0", port=8888)
    db = Database()  # 数据库处理对象
    dict.serve_forever()  # 启动服务
