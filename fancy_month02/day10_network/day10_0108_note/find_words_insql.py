import re
import pymysql
from socket import *
class Dict:
    def __init__(self):
        self.kwargs = {
            'host': "localhost",
            'port': 3306,
            'user': "root",
            'password': '123456',
            'database': 'dict',
            'charset': 'utf8'
        }
        self.connect()

    def connect(self):
        self.database = pymysql.connect(**self.kwargs)
        self.cur = self.database.cursor()

    def close(self):
        self.cur.close()
        self.database.close()

    # def insert_words(self, filename):
    #     file = open(filename)
    #     words = []
    #     for line in file:
    #         tmp = re.findall(r'(\w+)\s+(.*)', line)
    #         print(tmp)
    #         words += tmp
    #     file.close()
    #     self.insert_data(words)
    #
    # def insert_data(self, words):
    #     try:
    #
    #         sql = 'insert into words (word,mean)' \
    #               'values (%s,%s);'
    #         self.cur.executemany(sql, words)
    #         self.database.commit()
    #     except Exception as e:
    #         print(e)
    #         self.database.rollback()
class Udp_network:
    def __init__(self):
        self.S_ADDR =('127.0.0.1',8888)
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.dict = Dict()
    def req_to_sql(self,word):
        while 1:
            self.udp_socket.sendto(word.encode(), self.S_ADDR)
            sql = 'select word,mean from words where word=%s;'
            self.dict.cur.execute(sql, [word])
            word_mean = self.dict.cur.fetchall()
            return word_mean
            # udp_socket.sendto(msg.encode(), S_ADDR)
            # if msg == "##":
            #     break
            # data, addr = udp_socket.recvfrom(258)
            # print("从服务器%s收到%s" % (addr, data.decode()))



if __name__ == '__main__':
   dic = Dict()
   udp = Udp_network()

   dic.connect()
   print(udp.req_to_sql('zoo'))











"""

         
         
         
         
server
socket
    收客户消息
    连接mysql
    回给客户端
pymysql



"""


# tcp 1
# 多任务进程23
# 线程4
# 文件服务器\io 5



#draft-----------------------------------------------------------
# '''
# database = pymysql.connect(**kwargs)
# cur = database.cursor()
#
# data = [
#     ('ai','18','m',45),
#     ('bi','18','f',61),
#     ('ci','18','m',32),
#
# ]
#
#
# try:
#
#     sql= 'insert into class (name,age,sex,score)' \
#          'values (%s,%s,%s,%s);'
#     cur.executemany(sql,data)
# except Exception as e:
#     print(e)
#     database.rollback()
# database.commit()
#
#
#
# cur.close()
# database.close()
# '''
