"""
    练习3：
    需求：
        定义函数，在员工列表中查找部门编号是9001的员工数量
        定义函数，在员工列表中查找姓名字数大于2的员工数量
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数get_count
        3. 在当前模块中调用
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


def get_count01():
    count = 0
    for item in list_employees:
        if item.did == 9001:
            count += 1
    return count


def get_count02():
    count = 0
    for item in list_employees:
        if len(item.name) > 2:
            count += 1
    return count


count = get_count01()
print(count)
print(get_count02())

def condtion01(item):
    return item.did == 9001

def condtion02(item):
    return len(item.name) > 2

"""
def get_count(condition):
    count = 0
    for item in list_employees:
        # if len(item.name) > 2:
        # if condtion02(item):
        if condition(item):
            count += 1
    return count
"""

print(IterableHelper.get_count(list_employees,condtion01))