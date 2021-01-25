"""
    函数装饰器
"""
def new_func(func):
    def wrapper():
        print("新功能")
        func()
    return wrapper

@new_func # func01 = new_func(func01)
def func01():
    print("原函数")

func01()


# property 属性属于一种内置装饰器
class Wife:
    def __init__(self, age=0):
        self.age = age

    @property  #  age = property(age)
    def age(self):
        return self.__age

    @age.setter # age = age.setter(age)
    def age(self, value):
        self.__age = value

w01 = Wife(30)
print(w01.age)