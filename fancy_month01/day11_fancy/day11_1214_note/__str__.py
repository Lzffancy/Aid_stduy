#
class Car:
    def __init__(self,brand="None",speed=0):
        self.brand = brand
        self.speed = speed
    def __str__(self):
        return '你好！我是_str_'

car01 = Car()
print(car01)

class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price
    def __str__(self):
        return r"直接打印商品对象: %s的编号是%d,单价是%d" %(self.name,self.cid,self.price)
class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp
    def __str__(self):
        return r"直接打印敌人对象: %s的攻击力是%d,血量是%d" %(self.name,self.atk,self.hp)




commodity01 = Commodity()
enemy01 = Enemy("钢铁侠",9999,100)
print(commodity01,'\n',enemy01)