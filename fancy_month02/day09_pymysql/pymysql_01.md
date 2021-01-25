# Pymysql

## 1.基本操作

* pymysql使用流程
  from pymysql import *

  kwargs= {

  host ：主机地址,本地 localhost
  port ：端口号,默认3306
  user ：用户名
  password ：密码
  database ：库
  charset ：编码方式,推荐使用 utf8}

1. 建立数据库连接：db = pymysql.connect(**kwargs)

   

   

2. 创建**游标对象**：cur = db.cursor()      

   #返回游标对象,用于执行具体SQL命令

3. 游标方法:  cur.execute("insert ....",[...] )
   

4. 提交到数据库或者获取数据 :  db.commit() / cur.fetchall()

5. db.commit() 提交到数据库执行，必须支持事务操作才有效

   

6. 关闭游标对象 ：cur.close()

7. 断开数据库连接 ：db.close()

```
cur.executemany(sql命令,args_list)
功能： 多次执行SQL命令，执行次数由列表中元组数量决定
参数： sql sql语句
      args_list  列表中包含元组 每个元组用于给sql语句传递参量，一般用于写操作。
    args_list = [
    ('ai','18','m',45),
    ('bi','18','f',61),
    ('ci','18','m',32),]
    
    
```

cur.fetchone() 获取查询结果集的第一条数据，查找到返回一个***元组***否则返回None

cur.fetchmany(n) 获取前n条查找到的记录，返回结果为元组嵌套元组， ***((记录1),(记录2))***，查询不到内容返回***空元组***。

cur.fetchall() 获取所有查找到的记录，返回结果形式同上。