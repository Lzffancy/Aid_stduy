"""
    练习6:
        需求：
            定义函数,根据薪资对员工列表进行降序排列
            定义函数,查找员工编号对员工列表进行降序排列
        步骤：
            1. 根据需求，写出函数。
            2. 因为主体逻辑相同,核心算法不同.
            3. 在IterableHelper中创建函数descending order
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
def descending_order01():
    # 取数据
    for r in range(len(list_employees) - 1):
        # 作比较
        for c in range(r + 1, len(list_employees)):
            # 发现更大
            if list_employees[r].money < list_employees[c].money:
                # 则交换
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

def descending_order02():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].eid < list_employees[c].eid:
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]
"""

IterableHelper.descending_order(list_employees,lambda item:item.money)

for item in list_employees:
    print(item.__dict__)
