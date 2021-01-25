#---farme--
class Grenade:
    def boom(self,target):
        print('ＢＯＯＭ！！')
        target.damge_volue()  #!!!!!!!!!!!!!!!　１．编译调用父　　２．运行执行子　　

class Target:
    #def damge_volue(self):
     print("1")

#----target---------
class Person(Target):
    def damge_volue(self):# ２．子重写
        print("person.hp-100")
class Duck(Target):
    def damge_volue(self):
        print("duck.hp-999")
class House(Target):
    def damge_volue(self):
        print("House.hp-1")

g1 = Grenade()
# ３．创建子
t1 = Duck()
g1.boom(t1)

#如此设计可以以　类为单位　添加新的伤害对象