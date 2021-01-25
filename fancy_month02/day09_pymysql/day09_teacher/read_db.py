"""
数据库读操作示例  select
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

# 数据库数据的获取  select
sql = "select name,age,score from " \
      "class where score>%s;"
cur.execute(sql,[90])

for row in cur:
    print(row)

# 获取所有结果
# all = cur.fetchall() #  ()  ((..),(..))
# print(all)

# 第一个查询结果
# one = cur.fetchone() #  None  (..)
# print(one)

# many = cur.fetchmany(2)
# print(many)


# 关闭
cur.close()
db.close()
