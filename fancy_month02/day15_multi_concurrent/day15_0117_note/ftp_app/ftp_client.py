"""
ftp client
Author:Fancy
Email : 404notfind
Date: 2021-1-17
Env:Python 3.6

"""
import time
from socket import *
import sys,os


class ClientReady():
    # 初始化配置客户端,连接服务器
    def __init__(self):
        self.S_ADDR = ('127.0.0.1', 65530)
        self.socket_c = socket(AF_INET, SOCK_STREAM)

    # 返回套接字,供其他功能使用

    def get_socket(self):
        self.socket_c.connect(self.S_ADDR)
        return self.socket_c


class Handle():
    def __init__(self):
        # 实例化，获取socket
        self.client = ClientReady()
        self.sock = self.client.get_socket()


    def do_list(self):
        self.sock.send(b'LIST')
        res = self.sock.recv(128)
        # 收到ok则列表存在
        # print(res)
        if res == b'OK':
            files = self.sock.recv(1024 * 1024)
            print(files.decode())
        else:
            print('list request FAIL,please try again.\n')

    def do_exit(self):
        self.sock.send(b"EXIT")
        self.sock.close()
        sys.exit("thanks,bey~~")

    def do_get(self, file_name):
        # 拼接为协议格式
        req = ('GET %s' % file_name).encode()
        self.sock.send(req)
        # 接收 服务器 判断文件状态
        res = self.sock.recv(128)
        if res == b'OK':
            with open(file_name, 'wb') as f:
             while 1:
                data = self.sock.recv(1024)
                # 判断结束位
                if data == b"##":
                    break
                f.write(data)
            print("download %s complete\n" % file_name)
        elif res == b'FAIL':
            print("file %s not exist\n" % file_name)
        else:
            print("unexpect ERROR\n")

    def do_put(self, file_name):
       if  os.path.exists(file_name):
            req = ('PUT %s' % file_name).encode()
            self.sock.send(req)
            res = self.sock.recv(128)
            if res == b'OK':
                with open(file_name, 'rb') as f:
                    while 1:
                        data = f.read(1024)
                        # 判断结束位
                        if not data:
                            self.sock.send(b'##')
                            break
                        self.sock.send(data)
                print("upload %s complete"% file_name)
            elif res == b'FAIL':
                print("upload FAIL")
                print("file %s exist" % file_name)
                print("try other filename\n")
       else:
           print('local file %s not exist\n'%file_name)

class View():
    def __init__(self):
        self.__handle = Handle()

    def __show_menu(self):
        print("what do you want me do ?\n"
              " 1.list\n"
              " 2.download\n"
              " 3.upload\n"
              " 4.exit"
              )

    def __select(self):
        select = input("please input number by your keyboard.\n>>")
        if select == '1':
            self.__handle.do_list()
        elif select == '2':
            file_name = input('>>download file name:')
            self.__handle.do_get(file_name)
        elif select == '3':
            file_name = input('>>upload file name:')
            self.__handle.do_put(file_name)
        elif select == '4':
            self.__handle.do_exit()
        else:
            print("\nERROR:no such selection <%s>\n" % select)

    def main(self):
        while 1:
            self.__show_menu()
            self.__select()


if __name__ == '__main__':
    ftp_sever = ClientReady()
    ftp_view = View()
    ftp_view.main()
