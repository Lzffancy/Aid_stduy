import re
import pymysql
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

    def insert_words(self, filename):
        file = open(filename)
        words = []
        for line in file:
            tmp = re.findall(r'(\w+)\s+(.*)', line)
            print(tmp)
            words += tmp
        file.close()
        self.insert_data(words)

    def insert_data(self, words):
        try:

            sql = 'insert into words (word,mean)' \
                  'values (%s,%s);'
            self.cur.executemany(sql, words)
            self.database.commit()
        except Exception as e:
            print(e)
            self.database.rollback()


if __name__ == '__main__':
    dict = Dict()
    dict.insert_words('dict.txt')
    dict.close()



#面向对象 调用 方法干事情























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
