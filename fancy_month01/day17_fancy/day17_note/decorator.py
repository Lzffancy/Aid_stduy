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
func01 = new_func(func01) # 此时执行了新功能与原函数(不写ｗｒａｐｐｅｒ时候）

func01()

#-------????????---------------------------------------------------------------
def new_func(func):
    def wrapper(*args,**kwargs):
        verify_permissions()
        return func(*args,**kwargs)
    return wrapper

def verify_permissions():
    print("验证权限")
@new_func  #insert = new_func(insert)
def insert(string=''):
    print("插入")
    return "插入",string

@new_func
def delete():
    print("删除")
    return 404

# insert()
# delete()
# def new_func(func):
#     def wrapper():
#         verify_permissions()
#         func()
#     return wrapper


#insert = new_func(insert)
#delete = new_func(delete)
delete()
a = insert('你好')
print(a)
#------------------------------------------------------
import time



def time_func(func):
    def wrapper(n):
        start_time =time.time()
        result = func(n)
        end_time = time.time()
        return end_time-start_time,result
    return wrapper

@time_func     # sum_number =time_func(sum_number)
def sum_number(n):
    sum_value = 0
    for i in range(n):
     sum_value += i
    return sum_value


print(sum_number(100000000))


