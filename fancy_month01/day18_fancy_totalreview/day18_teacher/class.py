"""
    面向对象
        完整流程
            现实生活  -抽象->  类   -具体->  对象
             老婆        class Wife    Wife("建宁")
        创建类
            class 类名:
                类变量 = 数据

                @classmethod
                def 类方法(cls):
                    ...

                def __init__(self,参数):
                    self.实例变量 = 参数

                def 实例方法(self):
                    ...

                @staticmethod
                def 静态方法():
                    ...
        使用
            对象名 = 类名(数据)
            对象名.实例变量
            对象名.实例方法()

            类名.类方法()
            类名.静态方法()

        属性
            作用:保护实例变量
            适用性:实例变量取值需要控制在一定范围内
            注意:属性操作的都是私有变量
            语法:1. 读写属性
                2. 只读属性

        MVC软件架构
          　Model数据模型   View界面视图  Controller业务控制
           强调:显示与控制分离
"""


# 　读写属性
class MyClass:
    def __init__(self, data=""):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


m01 = MyClass()
print(m01.data)


# 只读属性
class MyClass:
    def __init__(self, data=""):
        self.__data = data

    @property
    def data(self):
        return self.__data


m01 = MyClass()
print(m01.data)


class XXController:
    def func01(self):
        print("func01执行了")


class XXView:
    def __init__(self):
        self.__controller = XXController()

    def func02(self):
        print("func02执行了")
        self.__controller.func01()


view = XXView()
view.func02()
