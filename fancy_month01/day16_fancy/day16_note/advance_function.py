"""
    内置高阶函数
"""


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1002, 9001, "悟空", 50000),
    Employee(1002, 9001, "悟空", 50000),
    Employee(1002, 9001, "悟空", 50000),
    Employee(1005, 9001, "小白龙", 15000),
]

# 1. map 映射
# 获取所有员工姓名  select
for name in map(lambda item: item.name, list_employees):
    print(name)

# 2.filter 过滤
# 获取所有员工姓名  find_all
for emp in filter(lambda item: item.did == 9001, list_employees):
    print(emp.__dict__)

# 3.min 最小  max 最大
# 获取薪资最低的员工
e = min(list_employees, key=lambda emp: emp.money)
print(e.__dict__)

# 4. sorted  排序
# 根据薪资升序排列
# 注意:通过返回值,返回排序后结果,不修改原列表
res = sorted(list_employees,key=lambda emp: emp.money)
for item in res:
    print(item.__dict__)

# 根据薪资降序排列
res = sorted(list_employees,key=lambda emp: emp.money,reverse=True)
for item in res:
    print(item.__dict__)