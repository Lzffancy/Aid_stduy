"""
    练习:
     让员工类返回底薪,
     程序员/测试员使用扩展重写.
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

#-----------------------------------
class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# ---------程序员--------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    # 后做
    def calculate_salary(self):
        return super().calculate_salary() + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() + self.bug_count * 5


# ---------入口--------------
manager = EmployeeManager()
manager.add_employee(Programmer(10000, 1000000))
manager.add_employee(Tester(8000, 500))
print(manager.get_total_salary())
