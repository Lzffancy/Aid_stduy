"""
    需求：小明使用手机打电话
    识别对象：
            人类        手机
    分配职责：
            打电话      通话
    建立交互：
           人类  调用  手机
"""
#------------------------------
class Person:
    def __init__(self, name=""):
        self.name = name
    def use(self,some_phone):
        some_phone.to_call()    # 继承父，调用子
#-----------------------------
class Some_phone:               # 父类　规范　
    def to_call(self,name):
     pass
#---------------------------
class MobilePhone(Some_phone):  #子重写
    def to_call(self):
        #super().__init__(name)怎么取得name ?
        print("移动电话呼叫")

class LocalPhone(Some_phone):
    def to_call(self):

        print( "座机电话呼叫")
class SatellitePhone(Some_phone):
    def to_call(self):

        print("卫星电话呼叫")
class NetPhone(Some_phone):
    def to_call(self):

        print("网络电话呼叫")

xm = Person("小明")
#创建子
localphone1 = MobilePhone()
xm.use(localphone1)

#创建person　　some_phone  和手机类型　　　封装
#MobilePhone(Some_phone)　　　　继承父类规范
#