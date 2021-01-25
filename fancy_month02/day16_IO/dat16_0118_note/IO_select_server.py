"""
基于select 的io 多路复用
"""
from socket import *
from select import select

IP = '0.0.0.0'
PORT = 65535
ADDR = (IP, PORT)


def sock_tcp():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(20)
    # 与非阻塞IO    防止io处理过程中产生阻塞（网络传输过程中延迟）
    # 绑定地址后才可以　设置非阻塞
    sock.setblocking(False)
    print("listen the port %d" % PORT)
    return sock


def select_io(sock):
    # 设置IO监听

    rlist = [sock]
    wlist = []
    xlist = []
    while 1:
        rs, ws, xs = select(rlist, wlist, xlist)
        for s in rs:
            if s is sock:
                connfd, addr = rs[0].accept()
                print("Connect from ", addr)
                connfd.setblocking(False)
                rlist.append(connfd)
            else:

                data = s.recv(1024)
                if not data:
                    rlist.remove(s)
                    s.close()
                    print("Exit", s)
                    continue
                print(s)
                print(data.decode())
                # 收到消息后设置该　连接套接字为　写就绪　添加监听
                wlist.append(s)

        for w in ws:
            w.send(b"OK")
            wlist.remove(w)


def main():
    sock = sock_tcp()
    select_io(sock)


if __name__ == '__main__':
    main()
