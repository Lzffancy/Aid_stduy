"""
{"key":"value"}
key: 几岁
value ： 我2岁啦

对话小程序，客户端可以发送问题给服务端
服务端接收到问题 将对应答案给客户端，客户端打印出来
要求可以同时多个客户端提问，如果问题没有指定答案
则回答 “人家还小，不知道。”
"""
from socket import *

# 对话字典
chat = {
    "你好":"你好啊！",
    "叫什么":"我叫小美",
    "男生女生":"我是机器人啦",
    "你几岁":"我2岁啦"
}

def handle(connfd):
    # q 客户端问题
    q = connfd.recv(1024).decode()
    for key,value in chat.items():
        if key in q:
            connfd.send(value.encode())
            break
    else:
        connfd.send("人家还小不知道啦。".encode())

def main():
    sock = socket()
    sock.bind(("0.0.0.0",8888))
    sock.listen(5)
    # 循环处理对话
    while True:
        connfd,addr = sock.accept()
        handle(connfd) # 接收问题回答问题
        connfd.close()

if __name__ == '__main__':
    main()




