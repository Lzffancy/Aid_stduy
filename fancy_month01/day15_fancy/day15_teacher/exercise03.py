class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


# 练习1:创建函数,在员工列表中查找部门是9002的所有员工
def get_employees_by_did():
    for item in list_employees:
        if item.did == 9002:
            yield item


# 查找过程反复使用
# 测试
for emp in get_employees_by_did():
    print(emp.__dict__)

for emp in get_employees_by_did():
    print(emp.__dict__)

# 练习2:通过生成器表达式,在员工列表中查找部门是9002的所有员工
# 查找过程只使用一次
result = (item for item in list_employees if item.did == 9002)
for item in result:
    print(item.__dict__)


# 练习3:创建函数,在员工列表中查找薪资大于2w的所有员工
def get_employees_by_money():
    for item in list_employees:
        if item.money > 20000:
            yield item


for emp in get_employees_by_money():
    print(emp.__dict__)

# 结论:函数返回多个结果使用yield
# 缺点:获取数据不灵活(不能使用索引切片)
# 解决:将惰性操作 转为 立即操作
tuple_result = tuple(get_employees_by_money())
print(tuple_result[0].__dict__)

# 练习4:通过生成器表达式,在员工列表中查找薪资大于2w的所有员工
result = (item for item in list_employees if item.money > 20000)
for item in result:
    print(item.__dict__)


# 练习5:定义函数,在员工列表中查找姓名是猪八戒的员工
def get_employee_by_name():
    for item in list_employees:
        if item.name == "猪八戒":
            return item


emp = get_employee_by_name()
print(emp.__dict__)


# 练习6:定义函数,在员工列表中查找员工编号大于1003的所有员工
def get_employees_by_eid():
    for item in list_employees:
        if item.eid > 1003:
            yield item


for item in get_employees_by_eid():
    print(item.__dict__)
