
class Employee:           #数据打包生成个个数据对象
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]



#------这个函数返回了一个生成器，可以一个个的按照ｄｉｄ生成所找到的对象-----------------------------------------------
def did_find(did):
    for item in list_employees:
        if item.did == did:
           yield item

for each in did_find(9002):
    print(each.__dict__,'did_find')
#--生成器表达式-单次使用---------------------------
result = (item
          for item in list_employees
          if item.did == 9002)

for each in result:
    print(each)

#-----------------------------------------
def high_salary_find(salary):
    '高薪是２００００以上'
    for item in list_employees:
        if item.money > salary:
           yield item
#这里用ｌｉｓｔ 和　tuple　去接　逐个生成下来的　结果
#解决:将惰性操作 转为 立即操作
print(list(high_salary_find(20000)))
print(tuple(high_salary_find(20000)))
#
for each in high_salary_find(20000):
    print(each.__dict__,'high_salary')
#------------------------------------------

#----返回单个用ｒｅｔｕｒｅｎ----------------------
def name_find(name=''):
    for item in list_employees:
        if item.name == name:
            return item

print(name_find('猪八戒').__dict__,'姓名查找')

#----------------------------------------------
result = (item
          for item in list_employees
          if item.eid > 1003)
for each in result:
    print(each.__dict__,'员工编号＞１００３')