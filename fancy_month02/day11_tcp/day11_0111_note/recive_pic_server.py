"""
receive file server
"""
from socket import *


def recv_file(connfd,save_path):
    with open(save_path, 'wb') as save_pic:
        while 1:
            r_data = connfd.recv(1024)
            # 判断结束位
            if r_data == b"##":
                break
            save_pic.write(r_data)
        connfd.send(b'ok,thanks,receive all succeed!')
        print('accpet over')


def main(save_path):
    tcp_socket_s = socket(AF_INET, SOCK_STREAM)
    tcp_socket_s.bind(('0.0.0.0', 65534))
    tcp_socket_s.listen(20)

    while 1:
        print('waiting for connect...')
        c_connfd, c_addr = tcp_socket_s.accept()
        print('ok,connet from', c_addr, '生成客户端连接套接字')
        recv_file(c_connfd,save_path)
        c_connfd.close()


if __name__ == '__main__':
    save_path = "/home/tarena/桌面/share/server_recive/20210111.jpeg"
    main(save_path)
