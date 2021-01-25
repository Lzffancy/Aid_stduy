"""
dict 服务端数据处理
"""
import pymysql
import hashlib


# 密码加密方法
def hash_encrytion(passwd):
    hash = hashlib.sha256(b"#*)^#")
    hash.update(passwd.encode())
    return hash.hexdigest()


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

    # 完成数据库连接
    def connect(self):
        self.db = pymysql.connect(**self.kwargs)

    def cursor(self):
        self.cur = self.db.cursor()

    # 关闭
    def close(self):
        self.db.close()

    # 注册
    def register(self, name, password):
        password = hash_encrytion(password)
        try:
            sql = "insert into user (name,passwd) values (%s,%s);"
            self.cur.execute(sql, [name, password])  # 向sql语句传递值
            self.db.commit()  # 提交事务
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False

    # 登录
    def login(self, name, password):
        password = hash_encrytion(password)
        sql = "select name from user where binary name=%s and binary passwd=%s;"
        self.cur.execute(sql, [name, password])
        if self.cur.fetchone():
            return True
        else:
            return False

    # 查询单词
    def query(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        # 获取结果  None  (mean,)
        mean = self.cur.fetchone()
        if mean:
            return mean[0]
        else:
            return "Not Found!"

    # 插入历史记录
    def insert_hist(self, name, word):
        # id  word  time user_id
        sql = "select id from user where name=%s;"
        self.cur.execute(sql, [name])
        id = self.cur.fetchone()[0]  # 用户id

        try:
            sql = "insert into hist (word,user_id) values (%s,%s);"
            self.cur.execute(sql, [word, id])
            self.db.commit()
        except:
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
