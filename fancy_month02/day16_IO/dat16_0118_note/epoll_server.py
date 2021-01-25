"""
epoll server
EPOLLOUT = 4
EPOLLIN = 1
"""
from select import *
from socket import *

IP = '0.0.0.0'
PORT = 65535
ADDR = (IP, PORT)


def sock_tcp():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(20)
    # 与非阻塞IO    防止io处理过程中产生阻塞（网络传输过程中）
    # 绑定地址后才可以　设置非阻塞
    sock.setblocking(False)
    print("listen the port %d" % PORT)
    return sock


def epoll_io(sock):
    ep = epoll()
    ep.register(sock, EPOLLIN | EPOLLET)
    # 字典存放了　文件描述符和　套接字的映射关系（register)
    e_map = {sock.fileno(): sock}

    while 1:
        events = ep.poll()  # events->[(fileno,event)]
        # for 循环取[(fileno,event)]!!
        for fd, event in events:
            # fd文件描述符
            # 建立连接－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
            if fd == sock.fileno():
                connfd, addr = e_map[fd].accept()
                print("Connect from ", addr)
                # 无阻塞连接　套接字，存在网络延迟的时候不等待
                connfd.setblocking(False)
                # 连接套接字加入关注
                ep.register(connfd, EPOLLIN | EPOLLET)  # IO只会提交一次，如未处理，则下次轮询一起处理
                # 字典维护
                e_map[connfd.fileno()] = connfd
            # 处理收发，断开－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
            else:
                # 　从字典取出文件描述符的对应套字
                data = e_map[fd].recv(1024).decode()
                # 判断是否为客户　异常退出
                if not data:
                    ep.unregister(fd)
                    del e_map[fd]
                    continue
                print(data)
                e_map[fd].send(b'OK')

        print(e_map)
        print(events)


def main():
    sock = sock_tcp()
    epoll_io(sock)


if __name__ == '__main__':
    main()
