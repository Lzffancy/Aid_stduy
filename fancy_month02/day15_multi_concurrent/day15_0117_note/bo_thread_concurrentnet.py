"""
面向对象　多线程实现　并发网络  (重要）
"""
from socket import *
from threading import Thread
import sys


class Handle:
    def requset(self, req):
        print(req.decode())
        pass


class MultiThrC(Thread):
    def __init__(self, connfd):
        # self.handle = handle
        self.connfd = connfd
        self.handle = Handle()
        super().__init__(daemon=True)

    def run(self):
        # self.handle(self.connfd)
        while 1:
            req = self.connfd.recv(1024)
            if not req:  # 客户端异常退出
                break
            self.handle.requset(req)


class ServerReady:
    def __init__(self):
        self.ADDR = ('0.0.0.0', 65535)

        # 以下两句　单独封装为　一个方法 返回一个socket
        self.sock_tcp = socket(AF_INET, SOCK_STREAM)
        self.sock_tcp.bind(self.ADDR)

    def server_activate(self):
        self.sock_tcp.listen(20)
        print("Listen the port", self.ADDR)
        while 1:
            # 循环等待　客户端connect ,返回　客户端连接套接字　和　客户端地址
            try:
                connfd, addr = self.sock_tcp.accept()
                print("Connect from", addr)
            except KeyboardInterrupt:
                print("server exit!")
                sys.exit()
            t = MultiThrC(connfd)
            t.start()


if __name__ == '__main__':
    sever = ServerReady()
    sever.server_activate()

'''
#参考
#
HOST = '0.0.0.0'
PORT = 65535
ADDR = (HOST, PORT)


# 处理客户端请求
def handle(connfd):
    pass


# 服务入口
def main(func=None):
    # tcp 套接字,tcp服务器基本配置
    sock_tcp = socket(AF_INET, SOCK_STREAM)
    sock_tcp.bind(ADDR)
    sock_tcp.listen(20)
    print("Listen the port", ADDR)

    while 1:
        # 循环等待　客户端connect ,返回　客户端连接套接字　和　客户端地址
        try:
            connfd, addr = sock_tcp.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            print("server exit!")
            sys.exit()

        # 创建进程，处理客户端请求                    不等子
        p = Process(target=func, args=(connfd,), daemon=True)
        p.start()


if __name__ == '__main__':
    def handle(connfd):
        while 1:
            data = connfd.recv(1024)
            if not data:
                break
            print(data.decode())
        connfd.close()


    main(handle)

'''
