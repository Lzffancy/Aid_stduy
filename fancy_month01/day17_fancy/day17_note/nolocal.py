"""
    Enclosing  外部嵌套作用域
        内部函数能读取外部嵌套变量
        必须通过nonlocal声明才能修改
"""


def func01():
    # 局部变量:相对于全局而言
    # 外部嵌套变量:相对于内部函数
    a = 10
    print("func01")

    def func02():
        print("func02")
        print(a) # 可以读取外部嵌套变量

    func02()  # 调用内部函数

#func02()不能调用内部函数
func01()  # 调用外部函数


def func03():
    a = 10
    print("func03")

    def func04():
        print("func04")
        # a = 20 # 不能修改外部嵌套变量
        nonlocal a# 如果必须修改,需要通过nonlocal声明
        a = 20

    func04()
    print(a)

func03()