"""
tcp client
"""
from socket import *
#S_ADDR =('176.140.10.96',8888)
#S_ADDR =('176.140.10.105',55555)
S_ADDR =('127.0.0.1',65535)
#tcp socket
tcp_sockte_c =socket(AF_INET,SOCK_STREAM)
# connect to s_ip
tcp_sockte_c.connect(S_ADDR)



# send and recive

while 1:
    msg = input('向服务器发送:')
    tcp_sockte_c.send(msg.encode())
    re_data= tcp_sockte_c.recv(1024)
    print(re_data.decode())
    if msg=="##":
        tcp_sockte_c.close()
        break




