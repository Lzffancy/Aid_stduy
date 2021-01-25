import pymysql
kwargs ={
    'host':"localhost",
    'port':3306,
    'user':"root",
    'password':'123456',
    'database':'fancy_personal',
    'charset':'utf8'
}
database = pymysql.connect(**kwargs)   #实参一分多


#游标,使用sql操作数得到结果的对象
cur = database.cursor()



#注意引擎  myisam 不支持事物会立刻执行,   innodb 需要commit

#执行语句
try:
    #sql01  = 'delete from class where id=8;'
    sql02 = 'update class set score=%s where id=%s'
    #sql03 = 'insert into class values (id'
    #cur.execute(sql01)
    cur.execute(sql02,[10,13])
except Exception as e:
    print(e)
    database.rollback()
#数据库提交
database.commit()



cur.close()
database.close()