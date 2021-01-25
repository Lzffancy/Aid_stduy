"""
写一个类 ，类中需要有一个 注册方法 和 一个登录方法
通过这两个方法可以完成注册登录功能
注册的用户名 不能重复
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
        user_info =[user,password]
        try:
           sql = "insert into user(user,password)" \
                 "values (%s,%s)"
           self.cur.execute(sql,user_info)
           self.db.commit()
           return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return None



    # 登录
    def login(self,user,password):
        """
        :param user:  用户名
        :param password:  密码
        :return: bool
        """
        user_info = [user, password]
        sql = 'select * from user ' \
              'where user=%s and password=%s '
        self.cur.execute(sql, user_info)
        user_result = self.cur.fetchone()
        #self.db.commit()
        if user_result:
            return True
        else:
            return False


if __name__ == '__main__':
    user = User()
    print(user.register("fancy3", "123456789"))
    user.close()

    # user = User()
    # print(user.login("张三", "abc123"))
    # user.close()