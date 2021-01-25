"""
数据库查询语句测试
author =fancy
date = 20210123
在dict_db中使用
"""
import pymysql
class Database:
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

    def connect(self):
        self.db = pymysql.connect(**self.kwargs)

    def cursor(self):
        self.cur = self.db.cursor()

    def hist(self, name):
        sql = "select id from user where name=%s;"
        self.cur.execute(sql, [name])
        id = self.cur.fetchone()[0]  # 用户id

        try:
            sql = "select word,time from hist where user_id=%s;"
            self.cur.execute(sql, [id])
            self.db.commit()
            # ((),())
            result = self.cur.fetchall()  #(('zoo', datetime.datetime(2021, 1, 21, 17, 11, 9)),)
            #print(result,"结果")
            return result
        except Exception as e:
            print(e)
            self.db.rollback()

    def history(self, name):
        #  name  word  time
        sql = "select name,word,time " \
              "from user left join hist " \
              "on user.id=hist.user_id " \
              "where name=%s " \
              "order by time desc " \
              "limit 10;"
        self.cur.execute(sql, [name])
        return self.cur.fetchall()  # ((),())


if __name__ == '__main__':
    db01 =Database()
    db01.cursor()
    db01.hist(name="fancy")
    print(db01.history("fancy"))