"""
ftp server
Author:Fancy
Email : 404notfind
Date: 2021-1-17
Env:Python 3.6

"""
from socket import *
from threading import Thread
import sys, os, time

FTP_source = r'I:\AID2011\fancy_month02\day15_multi_concurrent\day15_0117_note\ftp_app\FTPsoure\/'
#FTP_source = r'/home/tarena/桌面/fancy_month02/day15_multi_concurrent/day15_0117_note/ftp_app/FTPsoure/'

class Handle:
    def __init__(self, connfd, addr):
        self.connfd = connfd
        self.addr = addr

    def requset_decode(self):
        # 解协议,区分type
        while 1:
            data = self.connfd.recv(1024).decode()
            print(data, self.addr)
            temp = data.split(' ')
            # req_type = temp[0]
            # req_data = temp[1]
            # 先判断是不是退出请求,（异常退出和正常EXIT）
            if not temp or temp[0] == "EXIT":
                print("EXIT", self.addr)
                break
            elif temp[0] == "GET":
                self.do_get(temp[1])
            elif temp[0] == "PUT":
                self.do_put(temp[1])
            elif temp[0] == "LIST":
                self.do_list()

    def do_list(self):

        filelist = os.listdir(FTP_source)
        if filelist:
            self.connfd.send(b"OK")

            # 延迟防止沾包
            time.sleep(0.1)
            # 发送文件列表
            files = "\n".join(filelist)
            self.connfd.send(files.encode())
        else:
            self.connfd.send(b"FAIL")

    def do_put(self,file_name):
        #file_name =file_name.split('/')[-1]
        file_name = FTP_source + file_name
        if os.path.exists(file_name):
            self.connfd.send(b"FAIL")
            print('upload FAIL',self.connfd)
        else:
            self.connfd.send(b"OK")
            with open(file_name, 'wb') as f:
                while 1:
                    data = self.connfd.recv(1024)
                    # 判断结束位
                    if data == b"##":
                        break
                    f.write(data)
                print('uploaded %s%s'%(file_name,self.connfd))


    def do_get(self, file_name):
        # 拼接为 路径+文件名 以便open
        file_name = FTP_source + file_name
        print(file_name)
        # 判断文件是否存在 再给客户端文件状态回复
        if os.path.exists(file_name):
            self.connfd.send(b'OK')
            time.sleep(0.1)
            # 按1024字节读取发送给客户端 每次
            with open(file_name, 'rb') as f:
                while 1:
                    data = f.read(1024)
                    # 判断结束位
                    if not data:
                        self.connfd.send(b'##')
                        break
                    self.connfd.send(data)
        else:
            self.connfd.send(b'FAIL')


class MultiThrC(Thread):
    def __init__(self, connfd, addr):
        self.connfd = connfd
        self.handle = Handle(connfd, addr)
        self.addr = addr
        super().__init__(daemon=True)

    def run(self):
        self.handle.requset_decode()
        self.connfd.close()
        print("Thread close", self.addr)


class ServerReady:
    def __init__(self):
        self.ADDR = ('0.0.0.0', 65535)
        # 以下两句　也可单独封装为　一个方法 返回一个socket
        self.sock_tcp = socket(AF_INET, SOCK_STREAM)
        self.sock_tcp.bind(self.ADDR)

    def s_activate(self):
        self.sock_tcp.listen(20)
        print("Listen the port", self.ADDR)
        while 1:
            # 循环等待　客户端connect ,返回　客户端连接套接字　和　客户端地址
            try:
                connfd, addr = self.sock_tcp.accept()
                print("Connect from", addr)

            # 服务器端用键盘　退出　^D
            except KeyboardInterrupt:
                print("server exit!")
                sys.exit()
            t = MultiThrC(connfd, addr)
            t.start()


if __name__ == '__main__':
    sever = ServerReady()
    sever.s_activate()
