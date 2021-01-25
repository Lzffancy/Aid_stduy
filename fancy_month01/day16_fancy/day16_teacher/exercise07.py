"""
    练习7:
        需求：
            定义函数,判断员工列表中是否存在员工编号相同的元素
            定义函数,判断员工列表中是否存在姓名相同的元素
        步骤：
            1. 根据需求，写出函数。
            2. 因为主体逻辑相同,核心算法不同.
            3. 在IterableHelper中创建函数is_repeat
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
    Employee(1002, 9001, "悟空", 50000),
    Employee(1005, 9001, "小白龙", 15000),
]

"""
def is_repeat01():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].eid == list_employees[c].eid:
                return True
    return False


def is_repeat02():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].name == list_employees[c].name:
                return True
    return False
"""

print(IterableHelper.is_repeat(list_employees,lambda item:item.eid))
