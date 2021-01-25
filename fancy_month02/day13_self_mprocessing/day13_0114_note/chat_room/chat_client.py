"""
chat client

Author:Fancy
Email : 404notfind
Date: 2021-1-14
Env:Python 3.6

socket and process exercise

服务器通信数据协议　UDP
requset_data 　　 第一位数字 为请求类型
    　　　　　　   第二位开始到结束　为用户数据

    requset== 0 　　　用户请求自命名登录
    request == 1 　　用户请求发送聊天信息
    request == 2  　用户请求退出
"""
SEVER_ADDR = ('127.0.0.1', 65535)
from socket import *
from multiprocessing import Process
import sys


def login(sock):
    """
    尝试以nick_name进入聊天室，
    如果重名将重新申请
    :param sock:
    :return:nick_name str
    """
    while True:
        nickname = input("what ID do you want to use in chatroom?\n")
        # 按照协议发送　请求类型0+数据
        login_data = '0' + nickname
        sock.sendto(login_data.encode(), SEVER_ADDR)
        result, addr = sock.recvfrom(1024)
        if result == b'ok':
            print('ok,you can use this name: ', nickname)
            return nickname
        else:
            print('name already use,try again')
    # 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　待添加　如果服务器未响应（未开启）　客户端返回　提示用户

# 子进程
def recv_msg(sock):
    '''
     将作为子程序运行
     打印收到的群聊消息
    :param sock:
    :return:none
    '''
    while True:
        recv_data, addr = sock.recvfrom(1024 * 10)
        recv_data = '\n' + recv_data.decode()
        print(recv_data, end='')


# 父进程　中的发送函数
def send_msg(nickname, sock):
    '''
    发送聊天信息，以及处理聊天退出
    发送'exit'退出
    :param nickname:
    :param sock:
    :return: none
    '''
    while True:
        print(nickname, '>>', end='')
        try:
          msg = input()
        except Exception:
          msg ='exit'
        #包装消息
        if msg == 'exit':
            # 按照协议发送　请求类型2+数据
           send_data = '2' + nickname
           #此函数作用于全局
           sock.sendto(send_data.encode(), SEVER_ADDR)
           sys.exit(r'your id:%s was exit' % nickname)
        else:
            # 按照协议发送　请求类型1+数据
           send_data = '1' + nickname + ":" + msg
           sock.sendto(send_data.encode(), SEVER_ADDR)


def main():
    '''
       建立与服务器连接
       :return: socket
       '''
    #父进程
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0",25535))
    user_name = login(sock)

    # sock.sendto(b"test connect",SEVER_ADDR)
    send_msg(user_name,sock)
    #设置为子进程recv_msg，随父进程send_msg结束而结束
    p = Process(target=recv_msg, args=(sock,),daemon=True)
    p.start()
    #time.sleep(30)

if __name__ == '__main__':
    main()
