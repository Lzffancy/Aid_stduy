"""
pymysql操作数据库模板
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

# 使用sql操作数据


# 关闭
cur.close()
db.close()