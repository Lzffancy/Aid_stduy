"""
socket_test.py
套接字  基础函数示例
"""

import socket

# 创建udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定地址

# 1. 网络地址  别人可以通过IP与其通信
udp_socket.bind(("172.40.91.124",8888))

# 2. 测试地址  另外一段只能也在这个计算机上使用测试地址通信
udp_socket.bind(("127.0.0.1",8888))

# 3. 万能地址 别人可以通过以上两种情形访问
udp_socket.bind(("0.0.0.0",8888))


