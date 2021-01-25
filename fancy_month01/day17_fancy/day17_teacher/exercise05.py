"""
    在原函数不变情况下,增加验证权限功能
    使用装饰器原理实现

"""
def insert():
    print("插入")

def delete():
    print("删除")

# 有外有内:内部函数可以让外部函数被调用时,延迟执行内部函数体
#         拦截insert调用时,不应该执行新旧功能
# 内使用外:需要同时执行新旧功能
# 外返回内:让内部函数可以供客户端代码重复调用
def verify_permissions(func):
    def wrapper():
        print("验证权限") # 执行新功能
        func()# 执行旧功能
    return wrapper

# 拦截
insert = verify_permissions(insert)
delete = verify_permissions(delete)

# 客户端代码
insert()
insert()
delete()