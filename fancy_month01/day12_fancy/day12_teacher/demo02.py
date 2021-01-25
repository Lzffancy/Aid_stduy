"""
    有一个公司有如下几种岗位
        程序员:底薪 + 项目分红
        测试员:底薪 + Bug * 5
        ...
    创建员工管理器
        1. 记录所有员工
        2. 提供计算总薪资的功能

    三大特征:
        封装:创建员工管理器/程序员/测试员
        继承:创建员工类,隔离员工管理器与程序员/测试员的变化
        多态:程序员/测试员重写计算薪资方法实现具体的薪资计算方式
    设计原则:
        开闭原则:增加新岗位(销售),不影响员工管理器
        单一职责:
            员工管理器负责统一处理所有员工
            程序员负责计算程序员薪资算法
            测试员负责计算测试员薪资算法
        依赖倒置:
            员工管理器调用员工,不调用程序员/测试员
        组合复用:
            员工管理器与员工薪资算法属于组合关系(连接)
            员工与程序员/测试员属于继承关系(统一)
"""


# ---------架构师--------------
class EmployeeManager:
    def __init__(self):
        self.__all_employee = []

    def add_employee(self, emp):
        self.__all_employee.append(emp)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__all_employee:
            # 先用
            # 1. 编码时:调用父
            #    运行时:执行子
            total_salary += item.calculate_salary()
        return total_salary


class Employee:
    def calculate_salary(self):
        pass


# ---------程序员--------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    # 后做
    def calculate_salary(self):
        return self.base_salary + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def calculate_salary(self):
        return self.base_salary + self.bug_count * 5


# ---------入口--------------
manager = EmployeeManager()
manager.add_employee(Programmer(10000, 1000000))
manager.add_employee(Tester(8000, 500))
print(manager.get_total_salary())