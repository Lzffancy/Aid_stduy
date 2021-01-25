import pymysql
kwargs ={
    'host':"localhost",
    'port':3306,
    'user':"root",
    'password':'123456',
    'database':'fancy_personal',
    'charset':'utf8'
}
database = pymysql.connect(**kwargs)
cur = database.cursor()

data = [
    ('ai','18','m',45),
    ('bi','18','f',61),
    ('ci','18','m',32),

]


try:

    sql= 'insert into class (name,age,sex,score)' \
         'values (%s,%s,%s,%s);'
    cur.executemany(sql,data)
except Exception as e:
    print(e)
    database.rollback()
database.commit()



cur.close()
database.close()