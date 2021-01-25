"""
server
"""

from socket import *
#bulid socket
udp_socket = socket(AF_INET,SOCK_DGRAM)

# bind address
udp_socket.bind(('0.0.0.0',65535))
while 1:
    #recive data   收到的是字节串  (阻塞)
    data,addr = udp_socket.recvfrom(258)
    print('从客户端%s 收到%s' %(addr,data.decode()))
    print('flag01')

    # 回信
    udp_socket.sendto(b"hello,im recived",addr)
    if data.decode() == "##":
        break

# 关闭
udp_socket.close()