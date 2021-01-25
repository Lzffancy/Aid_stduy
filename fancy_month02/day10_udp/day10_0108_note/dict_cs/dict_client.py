"""
client
查单词 ,socket
      接收用户输入
      发消息给服务器端

      收服务器结果
      向用户展示
"""

from socket import *
#S_ADDR=('127.0.0.1',8888)
class QueryWord():
    def __init__(self):
        self.S_ADDR=('127.0.0.1',8888)
        # 建立客户端的socket
        self.udp_s =socket(AF_INET,SOCK_DGRAM)

    def query(self,word):
       self.udp_s.sendto(word.encode(),self.S_ADDR)
       data,addr = self.udp_s.recvfrom(1024)
       return data.decode()

    def close_udp(self):
        self.udp_s.close()
if __name__ == '__main__':
    # QueryWord()实例化后就会建立客户端端udp socket
    query_word = QueryWord()
    while 1:
        word = input('请输入需要查找的单词:')
        if word == '':
            query_word.close_udp()
        print(query_word.query(word))