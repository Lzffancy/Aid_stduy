#公司员工管理系统
'''作业
1. 三合一
2. 当天练习独立完成
3. 员工信息管理系统
    (1)录入员工信息
    (2)显示员工信息
    (3)删除员工信息
    (4)修改员工信息

class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid # 员工编号
        self.did = did # 部门编号
        self.name = name # 姓名
        self.money = money # 薪资'''

class Employee_Model:
    def __init__(self, eid=0, did=0, name='', money=0):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name  # 姓名
        self.money = money  # 薪资
    def __str__(self):
        return str(self.__dict__)
class Employee_View:
    def __init__(self):
        self.__controller = Employee_Controller()  #构建类间调用记得加（）　桥

    def __dispalay_menu(self):
        print("按1键录入员工信息")
        print("按2键显示员工信息")
        print("按3键删除员工信息")
        print("按4键修改员工信息")
    def __select_menu(self):
        sel = input("输入需要执行的操作：")
        if sel == '1':
            self.__input_emp()
        elif sel == '2':
            self.__show_emps()
        elif sel == '3':
            self.__delect_emp()
        elif sel == '4':
            self.__modfiy_emp()
    def __input_emp(self):
        emp_info = Employee_Model()
        #self.eid = input('员工编号')  # 员工编号
        emp_info.did = int(input ("部门编号:")) # 部门编号
        emp_info.name = input ('姓名:') # 姓名
        emp_info.money = input ('薪资:') # 薪资
        self.__controller.add_emp(emp_info)
        print("添加成功")
    def __show_emps(self):
        for item in self.__controller.list_emps:
            print(item)    #表由model打包所以重写　ｍｏｄｅｌ的__str__

    def __delect_emp(self):
        eid  = int(input("删除：请输入员工的ｅid:"))
        if self.__controller.remove(eid):
            print("删除成功",eid)
        else:
             print("删除失败")
    def __modfiy_emp(self):
        emp = Employee_Model()
        emp.eid = int(input("员工编号"))
        emp.did = int(input("部门编号:"))  # 部门编号
        emp.name = input('姓名:')  # 姓名
        emp.money = input('薪资:')  # 薪资

        if self.__controller.update_emp(emp):
            print("修改成功")
        else:
            print("修改失败")

    def main(self):
      while 1:
        self.__dispalay_menu()
        self.__select_menu()


class Employee_Controller:#核心　　存储数据

    def __init__(self):
        self.__list_emps = []
        self.__start_eid = 10000

    @property
    def list_emps(self):
        return self.__list_emps
    def add_emp(self, emp):
        emp.eid = self.__start_eid
        self.__start_eid += 1
        self.__list_emps.append(emp)

    def remove(self, eid):
        for i in range(len(self.__list_emps)):
            if self.__list_emps[i].eid == eid:
                print('删除',self.__list_emps[i])
                del self.__list_emps[i]
                return True
        return False

    def update_emp(self, emp):
      for each in self.__list_emps:
          if each.eid == emp.eid:
              each.__dict__=emp.__dict__
              return True
      return False


#-----------------------
view = Employee_View()
view.main()