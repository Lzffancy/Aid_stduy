"""
epoll
"""
from select import *
from socket import *

tcp_sock = socket(AF_INET, SOCK_STREAM)
tcp_sock.bind(('0.0.0.0', 65534))
tcp_sock.listen(20)

file = open("log.txt", 'r+')
udp_sock = socket(AF_INET, SOCK_DGRAM)

# 建立epoll对象
ep = epoll()

# 添加关注对象
ep.register(udp_sock, EPOLLIN | EPOLLOUT)
ep.register(tcp_sock, EPOLLIN | EPOLLOUT)

# 　建立文件描述符　映射
e_map = {
    udp_sock.fileno(): udp_sock,
    tcp_sock.fileno(): tcp_sock
}

# 开始监控
events = ep.poll()
# 不在关注
ep.unregister(tcp_sock)
del e_map[tcp_sock.fileno()]
