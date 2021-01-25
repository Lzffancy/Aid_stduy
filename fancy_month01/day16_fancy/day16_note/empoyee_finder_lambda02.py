from common.iterable_tool import Iterable_tool


class Employee:           #数据打包生成个个数据对象
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money
list_employees = [
    Employee(9003, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1009, 9001, "小白龙", 15000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
    Employee(1002, 9002, "白骨精", 15000),
    Employee(1009, 9001, "小白龙", 15000),

]

# def is_reapt():
#     """"""
#     for r in range(len(list_employees)-1):  #取数据
#         for c in range(r+1,len(list_employees)):#做比较
#             if list_employees[r].name == list_employees[c].name:
#                 return  True
#             return  False
#
print(Iterable_tool.is_reapt(list_employees,lambda item:item.name),'有无重名')

#------------------------------------------------------------------------
def remove_duplicate():
    for r in range(len(list_employees) - 1,-1,-1):  # 取数据
        for c in range(r+2,len(list_employees)): #做比较
            if list_employees[r].name == list_employees[c].name:
               del list_employees[c]

remove_duplicate()
for each in list_employees:
    print(each.__dict__)











