"""
同时多个客户端给服务端发送消息
"""

from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8880))

# 设置为监听套接字
tcp_socket.listen(5)

# 循环连接 收发 断开 -》 每次发送消息都需要连接
while True:
    connfd,addr = tcp_socket.accept()

    data = connfd.recv(1024)
    print("收到:",data.decode())
    connfd.send(b"Thanks")
    connfd.close()

# 关闭套接字
tcp_socket.close()





