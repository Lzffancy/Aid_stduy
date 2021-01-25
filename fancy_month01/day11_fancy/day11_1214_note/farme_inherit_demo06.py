"""
    面向对象设计思想
        封装:创建人类与汽车类/飞机类
        继承:
        多态
"""


# -----------架构师-----------
class Person:
    def use(self, vehicle):
        print("去..")
        if isinstance(vehicle,Vehicle): #判断是否时子类实例
            vehicle.transport()


class Vehicle:
    """
        交通工具
    """

    def transport(self):
     pass

# -----------程序员-----------
class Car(Vehicle):
    def transport(self):
        print("嘟嘟嘟")

class Airplane(Vehicle):

    def transport(self):
        print("嗖嗖嗖")

p01 = Person()
c01 = Car()
a01 = Airplane()
p01.use(c01)
p01.use("大爷")
