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

















cur.close()
database.close()