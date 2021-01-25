"""
群聊聊天室客户端
"""
from socket import *
from multiprocessing import Process
import sys

# 服务器地址
SERVER_ADDR = ("124.71.188.218", 8888)


def login(sock):
    while True:
        name = input("请输入昵称:")
        # 组织请求
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), SERVER_ADDR)
        result, addr = sock.recvfrom(1024)
        if result == b"OK":
            print("进入聊天室")
            return name
        else:
            print("该昵称已存在")


# 子进程接收函数
def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024 * 10)
        # 格式处理
        content = "\n" + data.decode() + "\n发言："
        print(content, end="")


# 　父进程发送函数
def send_msg(sock, name):
    while True:
        try:
            content = input("发言：")
        except KeyboardInterrupt:
            content = "exit"
        # 表示退出
        if content == 'exit':
            msg = "EXIT " + name
            sock.sendto(msg.encode(), SERVER_ADDR)
            sys.exit("您已退出聊天室")
        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(), SERVER_ADDR)


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0",55224)) # 端口不要变
    name = login(sock)  # 请求进入聊天室
    # 子进程负责接收
    p = Process(target=recv_msg, args=(sock,), daemon=True)
    p.start()
    send_msg(sock, name)  # 发送消息


if __name__ == '__main__':
    main()
