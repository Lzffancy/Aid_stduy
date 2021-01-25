"""
数据库写操作示例

* 如果使用myisam不支持事务，则execute()后立即生效
* 如果使用innodb支持事务，则执行语句后需要commit
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

# 写数据库操作  insert  delete  update
try:
    sql = "delete from class where id=3;"
    cur.execute(sql)  # 执行语句
    sql = "update class set score=%s where name=%s;"
    cur.execute(sql,[98,"Tom"]) # 向sql语句传递值
    db.commit()  # 提交事务
except Exception as e:
    print(e)
    db.rollback()  # 事务回滚

# 关闭
cur.close()
db.close()
