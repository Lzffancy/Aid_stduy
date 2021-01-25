
from select import select
from socket import *
tcp_sock = socket()
tcp_sock.bind(('0.0.0.0',65535))
tcp_sock.listen(20)


file  = open("log.txt",'r+')
udp_sock = socket(AF_INET,SOCK_DGRAM)

print("监控IO")
while 1:
    rs,ws,xs =select([tcp_sock],[],[])
    if rs:
        print(rs)
    # print("rlist",rs)
    # print("wlist",ws)
    # print("xlist",xs)