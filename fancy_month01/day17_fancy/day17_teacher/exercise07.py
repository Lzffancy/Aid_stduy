"""
    使用装饰器实现
"""


def verify_permissions(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        return func(*args,**kwargs)
    return wrapper

@verify_permissions  # 调用外部函数
def insert():
    print("插入")

@verify_permissions  # 调用外部函数
def delete():
    print("删除")


insert() #　执行的是内部函数
delete()
