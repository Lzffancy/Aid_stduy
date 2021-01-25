"""
dict 服务端数据处理
"""
import pymysql
import hashlib
def hash_encrytion(passwd):
    hash = hashlib.sha256(b"")
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
            sql = "insert into user (name,password) values (%s,%s);"
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
        sql = "select name from user where binary name=%s and binary password=%s;"
        self.cur.execute(sql, [name, password])
        if self.cur.fetchone():
            return True
        else:
            return False
