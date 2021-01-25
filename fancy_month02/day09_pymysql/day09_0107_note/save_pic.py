"""
存取二进制数据
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

# 存储图片
# with open("left.png",'rb') as f:        #字节串使用二进制读取存储
#     data = f.read()
# sql = "update class set image=%s where id=4;"
# cur.execute(sql,[data])
# db.commit()

# 取出图片
sql = "select image from class where id=4;"
cur.execute(sql)
data = cur.fetchone()[0]
with open("xxx.png",'wb') as f:
    f.write(data)

# 关闭
cur.close()
db.close()