'''
server
socket
    收客户消息
pymysql
    连接mysql
    回给客户端
'''
from socket import *
import pymysql
class LinkDictsql:
    def __init__(self):
     self.kwargs ={'host':'localhost',
                   'port':3306,
                   'user':'fancy',
                   'password':'123456',
                   'database': 'dict',
                   'charset':'utf8'}
     #实例化的时候就连接 sql
     self.connect_sql()

    def connect_sql(self):
        #建立数据库连接
        self.db =pymysql.connect(**self.kwargs)
        # 建立游标执行sql语句
        self.cur = self.db.cursor()
    def close_sql(self):
        self.cur.close()
        self.db.close()
    def get_mean_by_word(self, word):
        sql ='select mean from words where word=%s;'
        self.cur.execute(sql,[word])
        tuple_mean = self.cur.fetchone()


        if tuple_mean:
            return tuple_mean[0]
        else:
            return 'not find in dict_sql'

class FindWord():
  def __init__(self):
      #建立服务器的socket
    self.udp_s =socket(AF_INET,SOCK_DGRAM)
      #服务器绑定地址端口
    self.udp_s.bind(('0.0.0.0',8888))
    self.dict_sql = LinkDictsql()
  def answer(self):
      #接收用户的查询
    req_word,req_addr = self.udp_s.recvfrom(1024)
      #调用sql函数查找单词
    result_mean= self.dict_sql.get_mean_by_word(req_word.decode())
      #将单词解释返回给用户
    self.udp_s.sendto(result_mean.encode(),req_addr)




if __name__ == '__main__':
   # FindWord()实例化后就会建立服务器端  udp socket
  find_word = FindWord()
   # 保持对客户单端的响应
  while 1:
       find_word.answer()