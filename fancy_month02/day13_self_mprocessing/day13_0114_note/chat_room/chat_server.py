"""
chat server
Author:Fancy
Email : 404notfind
Date: 2021-1-14
Env:Python 3.6

socket and process exercise
"""
from socket import *

HOST = '0.0.0.0'
PORT = 65535
ADDR = (HOST, PORT)
client_dict = {}  # {'user':'addr'}


def login_name(sock, data, addr):
    #print('登录判断', data)
    if data in client_dict:
        sock.sendto(b"not this name", addr)
    else:
        sock.sendto(b'ok', addr)
        # 给所有人发送欢迎信息
        for user, u_addr in client_dict.items():
            welcom_msg = 'welcom %s,say hello to everyone!' % data
            sock.sendto(welcom_msg.encode(), u_addr)
        # 新用户写入
        client_dict[data] = addr
        print(client_dict)


def chat(sock, data, addr):
    for user, u_addr in client_dict.items():
        # if user !=
        sock.sendto(data.encode(), u_addr)


def exit_chatroom(sock, name, addr):
     del client_dict[name]
     msg ="%s　exit chatroom!!" %name
     for key,value in client_dict.items():
         sock.sendto(msg.encode(),value)


def handle_data(sock):
    """
    requset_data 第一位数字 为请求类型
    　　　　　　   第二位开始　为用户数据
    :param sock:
    :return:
    """
    while True:
        print("server runing..")
        request, c_addr = sock.recvfrom(1024)
        # print(request.decode())
        request_data = request.decode()

        request = int(request_data[0]) # 请求类型标志位
        data = request_data[1:]        #　用户数据

        print(request, data)

        # 分情况讨论
        if request == 0:
            login_name(sock, data, c_addr)
        elif request == 1:
            chat(sock, data, c_addr)
        elif request == 2:
            exit_chatroom(sock, data, c_addr)


def main():
    # udp
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)
    handle_data(sock)  # 接收处理请求
    #　　　　　　　　　　　　　　　　　　　　　　　　　　　　待　添加　服务器管理员消息发送

if __name__ == '__main__':
    main()
