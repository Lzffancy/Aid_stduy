"""
    练习1:通过IterablHelper + Lambda实现
        在员工列表中查找部门编号是9001的所有员工
        在员工列表中查找员工编号是1003的员工
        在员工列表中查找月薪小于50000的员工数量
"""
from common.iterable_tools import IterableHelper


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


# lambda参数是:列表中的元素
for item in IterableHelper.find_all(list_employees,lambda item:item.did ==9001):
    print(item.__dict__)

# 如果不能直接写出lambda的同学,先使用def函数创造条件(对列表元素的处理逻辑)
# 最后在改写lambda
# def condition01(emp:Employee):
#     return emp.eid == 1003

item = IterableHelper.find_single(list_employees,lambda emp: emp.eid == 1003)
print(item.__dict__)

count = IterableHelper.get_count(list_employees,lambda element:element.money < 50000)
print(count)