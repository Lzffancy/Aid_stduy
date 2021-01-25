'''
数据库读
'''

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

sql  = 'select name,score from class where score>%s;'
cur.execute(sql,[80])

#all = cur.fetchall()
#print(all)
one = cur.fetchone()
print(one)
many = cur.fetchmany(2)
print(many)

for row in cur:
    print(row)
#database.commit()



cur.close()
database.close()