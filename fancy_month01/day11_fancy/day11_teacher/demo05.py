"""
    面向对象设计思想
        封装:创建人类与汽车类/飞机类
        继承
        多态
"""

# 需求:增加飞机,轮船,自行车...
# 缺点:违反开闭原则
# 增加飞机类的同时,还需要修改人类代码.
class Person:
    def use(self, vehicle):
        print("去..")
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("嘟嘟嘟")

class Airplane:
    def fly(self):
        print("嗖嗖嗖")

p01 = Person()
c01 = Car()
a01 = Airplane()
p01.use(c01)
