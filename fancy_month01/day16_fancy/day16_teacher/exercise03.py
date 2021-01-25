"""
    练习3:
        需求：
            定义函数，查找所有员工的姓名
            定义函数，查找所有员工的员工编号与工资
        步骤：
            1. 根据需求，写出函数。
            2. 因为主体逻辑相同,核心算法不同.
               所以使用函数式编程思想(分、隔、做)
               创建通用函数select
            3. 将通用函数定义在IterableHelper中
               在当前模块调用(使用lambda)
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

"""
def select01():
    for item in list_employees:
        yield item.name


def select02():
    for item in list_employees:
        yield item.eid, item.money


for name in select01():
    print(name)


def handle01(item):
    return item.name

def handle02(item):
    return item.eid, item.money

def select(handle):
    for item in list_employees:
        # yield item.eid, item.money
        # yield handle02(item)
        # yield handle01(item)
        yield handle(item)
"""

for item in IterableHelper.select(list_employees,lambda item:item.name):
    print(item)


for item in IterableHelper.select(list_employees,lambda item:(item.eid,item.money)):
    print(item)