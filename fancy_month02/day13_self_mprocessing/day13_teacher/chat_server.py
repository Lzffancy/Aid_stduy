"""
Author : Levi
Email : lvze@tedu.cn
Date : 2021-1-14
Env : Python3.6

socket and process exercise
"""
from socket import *
from multiprocessing import Process

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储用户信息 {name:address}
user = {}


# 处理进入聊天室
def login(sock, name, address):
    if name in user or "管理" in name:
        sock.sendto(b"FAIL", address)
    else:
        sock.sendto(b"OK", address)
        # 告知其他人
        msg = "欢迎 %s 进入聊天室" % name
        for key, value in user.items():
            sock.sendto(msg.encode(), value)
        user[name] = address  # 存储用户
        # print(user)  # 测试


# 处理聊天
def chat(sock, name, content):
    msg = "%s : %s" % (name, content)
    for key, value in user.items():
        # 不是本人就发送
        if key != name:
            sock.sendto(msg.encode(), value)


# 处理退出
def exit(sock, name):
    del user[name]  # 删除该用户
    # 通知其他用户
    msg = "%s 退出聊天室" % name
    for key, value in user.items():
        sock.sendto(msg.encode(), value)


def handle(sock):
    # 不断接收请求，分情况讨论
    while True:
        request, addr = sock.recvfrom(1024)
        tmp = request.decode().split(" ", 2)
        # 分情况讨论
        if tmp[0] == "LOGIN":
            # tmp ->[LOGIN,name]
            login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            # tmp ->[CHAT,name,content]
            chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "EXIT":
            # tmp ->[EXIT,name]
            exit(sock, tmp[1])


# 程序入口函数
def main():
    # 创建udp
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    # 接收请求，分类处理
    p = Process(target=handle,args=(sock,),daemon=True)
    p.start()

    while True:
        content = input("管理员消息:")
        if not content:
            break
        msg = "CHAT 管理员消息 " + content
        # 从父进程发送到子进程
        sock.sendto(msg.encode(),ADDR)




if __name__ == '__main__':
    main()
