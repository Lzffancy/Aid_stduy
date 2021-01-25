"""
TCP服务端函数示例
重点代码 ！！
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置为监听套接字
tcp_socket.listen(5)

# 等待客户端连接
while True:
    print("Waiting for connect...")
    connfd,addr = tcp_socket.accept()
    print("Connect from",addr)

    # 循环收发消息  客户端退出 recv立即返回b""
    while True:
        data = connfd.recv(5)
        # data=b""客户端直接关闭  b"##"客户端主动告知关闭
        if not data or data == b'##':
            break
        print("收到:",data.decode())
        connfd.send(b"Thanks/")
    connfd.close()

# 关闭套接字
tcp_socket.close()





