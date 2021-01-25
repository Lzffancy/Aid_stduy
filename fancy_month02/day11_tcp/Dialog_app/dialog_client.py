"""
接收用户问题 发 给服务器
接收服务答案 打印

多用户 会话一次连接一次 断开一次
"""
from socket import *


class Dialog_client():
    # 初始化配置客户端,连接服务器
    def __init__(self):
        self.S_ADDR = ('127.0.0.1', 65534)
        self.socket_c = socket(AF_INET, SOCK_STREAM)

    def sent_req(self):
        req_input = input("你想问什么?")
        self.socket_c.connect(self.S_ADDR)

        self.socket_c.send(req_input.encode())
        print(self.socket_c.recv(1024).decode())

        self.socket_c.close()


if __name__ == '__main__':
    while 1:
        dialog_c = Dialog_client()
        dialog_c.sent_req()

