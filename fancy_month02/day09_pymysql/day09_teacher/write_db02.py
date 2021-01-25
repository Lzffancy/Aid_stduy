"""
数据库批量写操作示例
"""
import pymysql

kwargs = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8"
}

# 连接数据库
db = pymysql.connect(**kwargs)

# 创建游标  使用sql操作数据得到结果的对象
cur = db.cursor()

# 写数据库操作

data = [
    ("Lily", 18, 'f', 90),
    ("Lucy", 17, 'f', 81),
    ("Tom", 19, 'm', 71)
]

try:
    sql = "insert into class (name,age,sex,score) " \
          "values (%s,%s,%s,%s);"

    cur.executemany(sql, data)

    # for item in data:
    #     cur.execute(sql,item)

    db.commit()  # 提交事务
except Exception as e:
    print(e)
    db.rollback()  # 事务回滚

# 关闭
cur.close()
db.close()
