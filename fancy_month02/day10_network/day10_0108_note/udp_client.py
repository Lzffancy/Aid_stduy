"""
client
"""
#S_ADDR =('176.140.10.96',8888)
#S_ADDR =('127.0.0.0',65535)
S_ADDR =('176.140.10.94',55555)

from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)


while 1:
   msg = input("发给服务器内容:")

   udp_socket.sendto(msg.encode(),S_ADDR)
   if msg =="##":
       break
   data,addr = udp_socket.recvfrom(258)
   print("从服务器%s收到%s" % (addr, data.decode()))


udp_socket.close()