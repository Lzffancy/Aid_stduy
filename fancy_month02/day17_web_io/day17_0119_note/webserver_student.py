"""
WebServer
Author:Fancy
Email : 404notfind
Date: 2021-1-19
Env:Python 3.6

给前端提供的　网页部署服务
IO并发
"""
from socket import *
from select import select





class WebServer():

    def __init__(self,host,port,html):
        self.host =host
        self.port =port
        self.html =html
        self.sock = self.create_socket()

        # 定义监控IO列表
        self.rlist = [self.sock]
        self.wlist = []
        self.xlist = []

    # 建立　socket　服务器初始化
    def create_socket(self):
        sock = socket()
        sock.bind((self.host,self.port))
        sock.setblocking(False)
        return sock
#-------------------------------------------
    def read_manager(self,rs):
        # 逐个取值，分情况讨论
        for r in rs:
            print("Waiting Connect....")
            # 处理连接
            if r is self.rlist[0]:
                connfd, addr = r.accept()
                print("Connect from", addr)
                # 将客户端套接字添加到监控列表
                connfd.setblocking(False)
                self.rlist.append(connfd)
            else:
                print('r')
                self.handle_response(r)
    def handle_response(self,r):
        # 处理接收到的HTTP　requset　(协议解析）
        print(r.recv(1024).decode)
        pass
    def write_manager(self,ws):
        for w in ws:
            # 组合HTTP　response　(协议编辑）
            w.send(b"OK")
            self.wlist.remove(w)  # 否则一直让你发送
#---------------------------------------------
    # def connect_client(self,r):
    #     connfd, addr = r.accept()
    #     print("Connect from", addr)
    #     # 将客户端套接字添加到监控列表
    #     connfd.setblocking(False)
    #     self.rlist.append(connfd)

    def start(self):
        # 设置套接字  IO监听　　保持
       self.sock.listen(5)
       print('Listen the port:',self.port)
       while 1:
        #print('监控中')
        rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
        self.read_manager(rs)  # 处理读操作
        self.write_manager(ws)  # 处理写操作

if __name__ == '__main__':
    # 先确定如何使用
    httpu =WebServer(host='0.0.0.0',port=65531,html='./static')
    httpu.start()
