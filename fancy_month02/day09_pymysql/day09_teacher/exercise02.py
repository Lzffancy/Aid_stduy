"""
写一个类 ，类中需要有一个 注册方法 和 一个登录方法
通过这两个方法可以完成注册登录功能
注册的用户名 不能重复
create table user (
id int primary key auto_increment,
user char(30) not null unique,
password char(64) not null
);
"""

import pymysql


class User:
    def __init__(self):
        self.kwargs = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "database": "stu",
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

    # 注册
    def register(self,user,password):
        """
        :param user:  用户名
        :param password:  密码
        :return: bool
        """
        try:
            sql = "insert into user (user,password) values (%s,%s);"
            self.cur.execute(sql, [user, password])  # 向sql语句传递值
            self.db.commit() # 提交事务
            return True
        except Exception as e:
            self.db.rollback()
            return False


    # 登录
    def login(self,user,password):
        """
        :param user:  用户名
        :param password:  密码
        :return: bool
        """
        sql = "select user from user where user=%s and password=%s;"
        self.cur.execute(sql,[user,password])
        if self.cur.fetchone():
            return True
        else:
            return False

if __name__ == '__main__':
    # user = User()
    # print(user.register("张三","abc123"))
    # user.close()

    user = User()
    print(user.login("张三", "abc12"))
    user.close()
