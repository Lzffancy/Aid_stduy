"""
TCP套接字编程 客户端
重点代码 ！！
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

# 使用默认值--》tcp
tcp_socket = socket()

# 发起连接
tcp_socket.connect(ADDR)

# 循环发送接收消息
while True:
    msg = input(">>")
    tcp_socket.send(msg.encode())
    # 结束发送
    if msg == "##":
        break
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())

tcp_socket.close()