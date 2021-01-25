"""
编写一个程序，将dict.txt单词本中的单词存储到
数据库中以的一个数据表里
"""
import pymysql
import re


class Dict:
    def __init__(self):
        self.kwargs = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "database": "dict",
            "charset": "utf8"
        }
        self.connect()

    # 完成数据库连接
    def connect(self):
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    # 关闭
    def close(self):
        self.cur.close()
        self.db.close()

    # 插入数据  提取文件中的单词
    def insert_words(self, filename):
        file = open(filename)
        words = []  # [(word,mean),(word,mean)...]
        for line in file:
            tmp = re.findall(r"(\w+)\s+(.*)", line)
            words += tmp  # 大列表
        file.close()
        self.insert_data(words)

    def insert_data(self, words):
        try:
            sql = "insert into words (word,mean) values (%s,%s);"
            self.cur.executemany(sql, words)
            self.db.commit()  # 提交事务
        except Exception as e:
            print(e)
            self.db.rollback()  # 事务回滚


if __name__ == '__main__':
    dict = Dict()
    dict.insert_words("dict.txt")  # 插入单词数据
    dict.close()
