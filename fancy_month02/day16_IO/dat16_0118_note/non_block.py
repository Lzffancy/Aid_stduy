from socket import *
from time import ctime

sock = socket()
sock.bind(("127.0.0.1",65533))
sock.listen(5)

# 设置非阻塞IO socket
# sock.setblocking(False)
sock.settimeout(3)
file = open ('log.txt','a')

while 1 :
    try:
        # 此处的sock.accept()将不会阻塞，程序继续向下执行
        # 做轮询操作，当有connect时仍然可以连接上
        connfd,addr = sock.accept()
        print("Connect from",addr)
    except (BlockingIOError,timeout) as error:
           msg ='%s:%s\n' %(ctime(),error)
           file.write(msg)

    else:
        data = connfd.recv(1024)
        print(data.decode())