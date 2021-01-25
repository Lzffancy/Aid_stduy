"""
    函数装饰器
        不改变原函数的定义和调用,为其增加新功能
        适用性:
            原函数与新功能不是固定调用关系
            而是经常需要改变
"""
def func01():
    print("原函数")

def new_func(func):
    def wrapper():
        print("新功能") # 执行新功能
        func() # 执行原函数
    return wrapper

# 拦截调用(不执行具体功能)
# func01 = new_func # 新功能覆盖了原函数
# func01 = new_func + func01 # 希望表达新功能与原函数同时执行
func01 = new_func(func01) # 此时执行了新功能与原函数(错误)

func01()
func01()