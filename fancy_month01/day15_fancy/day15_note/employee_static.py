from common.iterable_tool import Iterable_tool


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

def con01_did(item,number):
    return item.did ==  number

a_did = Iterable_tool.find_single(list_employees,con01_did,9002)
# def did_find(did):
#     for item in list_employees
#         if con01():
#            yield item
for each in a_did:
    print(each.__dict__,'did_find')




#--------------------------------------
# def get_count(did,condition):
#     count = 0
#     for item in list_employees:
#         if condition():
#             count += 1
#         return count

def count_did(item,did):
    return item.did == did
def who_namestr_bigthen(item,number):
    return len(item.name) > number




did_count = Iterable_tool.get_count(list_employees,con01_did,9001)
print(did_count)

namestr_bigthen =Iterable_tool.get_count(list_employees,who_namestr_bigthen,2)
print(namestr_bigthen)