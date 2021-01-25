"""
    函数装饰器-细节
        内部函数返回值：旧功能返回值
"""


def new_func(func):
    def wrapper(*args,**kwargs):  # 多合一
        print("新功能")
        re = func(*args,**kwargs)  # 一拆多 接收旧功能返回值
        return re  # 内部函数返回值：旧功能返回值

    return wrapper


@new_func
def func01(p1):
    print("原函数", p1)
    return 100


@new_func
def func02(p1, p2):
    print("原函数", p1, p2)


res = func01(10)  # 调用内部函数
print(res)
func02(10, 20)
func02(10, p2=20)
