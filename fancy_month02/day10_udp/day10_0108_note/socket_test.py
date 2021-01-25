"""
套接字 socket
建立通信
"""

import socket
#创建socket
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bind address  服务端需要进行绑定操作
udp_socket.bind(("176.140.10.93",1024))


#test address  本地测试环回
udp_socket.bind(("127.0.0.1",8888))


# 万能地址,别可用以上两种情况访问
udp_socket.bind(("0.0.0.0",8888))

# 阻塞函数
input()