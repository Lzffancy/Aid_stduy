"""
tcp server
"""

from socket import *
# tcp socket
tcp_socket_s = socket(AF_INET,SOCK_STREAM)
tcp_socket_s.bind(('0.0.0.0',65535))

""
#listen socket  看成一个列队设置
tcp_socket_s.listen(20)

#wait accept client
while 1:
    print('waiting for connect...')
    c_connfd,c_addr = tcp_socket_s.accept()  #与客户端connect呼应
    print('ok,connet from',c_addr,'生成客户端连接套接字',c_connfd)


    # recive and sendback
    while 1:
        re_data = c_connfd.recv(5)
        print('收到来自',c_addr,"的消息:",re_data.decode())
        c_connfd.send(b'ok,thanks')  #会产生BrokenPipeError
        # 异常关闭或主动关闭
        if re_data  == b"##" :
            print(c_addr,'退出')
            break
        elif not re_data:
            print(c_addr, '异常退出')
            break

    c_connfd.close()


