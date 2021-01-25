"""
    练习4:
        需求：
            定义函数,删除部门编号是9002的所有员工
            定义函数,删除薪资大于30000的所有员工
        步骤：
            1. 根据需求，写出函数。
            2. 因为主体逻辑相同,核心算法不同.
            3. 在IterableHelper中创建函数delete_all
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
def delete_all01():
    count = 0
    for i in range(len(list_employees) - 1, -1, -1):
        if list_employees[i].did == 9002:
            del list_employees[i]
            count += 1
    return count

def delete_all02():
    count = 0
    for i in range(len(list_employees) - 1, -1, -1):
        if list_employees[i].money > 30000:
            del list_employees[i]
            count += 1
    return count
"""

print(IterableHelper.delete_all(list_employees,lambda item:item.did == 9001))
for item in list_employees:
    print(item.__dict__)