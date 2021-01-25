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
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
    Employee(1008, 9002, "白骨精", 15000),
    Employee(1009, 9001, "如来佛", 15000),

]

d9001 = Iterable_tool.find_all(list_employees,lambda number:number.did == 9001)
for each in d9001:
    print(each.__dict__,'d9001')
e1003 = Iterable_tool.find_single(list_employees,lambda item:item.eid == 1003)
print(e1003.__dict__,'e1003')
salary_d_50000 = Iterable_tool.get_count(list_employees,lambda item:item.money <50000)
print(salary_d_50000)
#--------------------------------------------+
sum_salary = Iterable_tool.sum_all(list_employees,lambda a:a.money)  #def x(a)  return(a.money)
print(sum_salary)

sum_eid =  Iterable_tool.sum_all(list_employees,lambda item:item.eid)
print(sum_eid)
#草稿－－－－－－－－－－－－－－－－－－－－－－－
# def con(each):
#     return each.name
# def select(conx):
#     name_list = []
#     for item in list_employees:
#         name_list.append(conx(item))
#     return name_list
#---------------------------------------
selet_name = Iterable_tool.select(list_employees,lambda item:item.name)
print(selet_name)

selet_eid_salary = Iterable_tool.select(list_employees,lambda item:(item.eid,item.money))
print(selet_eid_salary)

#-----------------------
# def con(each):
#     return each.did==9002
# def select(conx):
#     for i in range(len(list_employees)-1,-1,-1):
#         if conx(list_employees[i                                                       ]):
#             del list_employees[i]

print(Iterable_tool.delete_all(list_employees, lambda item: item.did == 9002),'删除次数')

for each in list_employees:
    print(each.__dict__)
#----------------------------------------------
max_value =Iterable_tool.get_max(list_employees, lambda item: item.money)
print(max_value.__dict__,'最高工资')
#-------------
Iterable_tool.descending(list_employees, lambda item: item.money)
for each in list_employees:
    print(each.__dict__)