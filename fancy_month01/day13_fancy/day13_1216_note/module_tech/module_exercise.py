data = 100
def func01():
    print("func01执行喽")
class MyClass:
    def func02(self):
        print("func02执行喽")
    @classmethod    #类方法不仅可以MyClass.调用也可以实用该类的实例调用
    def func03(cls):
        print("func03执行喽")
