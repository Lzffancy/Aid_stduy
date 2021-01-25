#
class Persion:
   def __init__(self, name, ill):
       self.name = name
       self.ill = ill

   def go_hospital(self,department):
       print(self.name,'去医院啦')
       department.inquiry(self)                #开闭，该段 不允许改动




class Hospital_department:
    def __init__(self,name):  #此处给所有子类传递 患者名字
        self.name = name
    def inquriry(self):
         pass
    def count_bill(self):
        print("结算",self.name,"社保")




class Eye_department(Hospital_department):
    def inquiry(self):
        print(self.name,'在看眼科啦')
        Hospital_department.count_bill(self)         #类的单一职责 ，核算社保过程交给Hospital


class Mental_department(Hospital_department):
    def inquiry(self):
        print(self.name,'在看神经科啦')
        Hospital_department.count_bill(self)





#-----------入口-------------------------
hanmeimei = Persion("hmm",'青光眼')
hanmeimei.go_hospital(Eye_department)    #依赖倒置，病人不直接找Eye_department， 是先go_hospital