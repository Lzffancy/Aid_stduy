"""
    封装设计思想
        分而治之
        变则疏之

    1. 识别对象(寻找行为变化点的过程)
        数据不同:
            老张/老李/老孙 --> 人类
        行为不同:
            人类      汽车类
    2. 分配职责
            使用       行驶
    3. 建立交互
"""

# 需求:老张开车去东北

# 写法1:直接创建对象
# 语义:老张每次开use车新车去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name 
    def use(self, position):
        print("去", position)
        car = Car()        #！！！！！！！！！！！！！！！！！！！！！在use下实例化car
        car.run() 
class Car:
    def run(self):
        print("嘟嘟嘟...") 
# 用对象区分数据不同
lz = Person("老张")
ll = Person("老李")
ls = Person("老孙")

lz.use("东北")
lz.use("西北")
lz.use("xxx")
"""

# 写法2:在构造函数中创建对象
# 语义:老张开车自己的车去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()　　＃当新建一个Ｐ对象就有　ｐ.car = Car()对象　于是拥有run方法

    def use(self, position):
        print("去", position)
        self.car.run()    #！！！！！！！！！！！！！！

class Car:
    def run(self):
        print("嘟嘟嘟...")

 
lz = Person("老张") 
lz.use("东北")　　     #但是外部只能知道use
"""


# 写法3: 不创建对象,而是通过参数传递
# 语义:老张使用交通工具去东北
class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self, vehicle, position):   # 抽象化car->vehicle
        print("去", position)
        vehicle.run()


class Car:
    def run(self):
        print("嘟嘟嘟...")


lz = Person("老张")
car = Car()                  #  实例化car
lz.use(car, "东北")           # car对象作为参数传给Vehicle   ,再去调用run()
