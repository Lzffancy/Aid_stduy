"""
    函数式编程 - 语法
        函数可以赋值给变量，赋值后变量绑定函数
"""


def func01():
    print("func01执行了")


# 将函数返回值 赋值给 变量
# a = func01()
# 将函数 赋值给 变量,没有执行函数
a = func01

# 通过函数名直接调用函数
func01()
# 通过变量间接调用函数
a()


# 应用价值:将函数赋值给参数,将一段逻辑(条件)传入另一个函数
def func02():
    print("func02执行了")


def func03(func):
    print("func03执行了")
    func()  # 此时func03与哪个函数组合,不确定(灵活)


func03(func01)
func03(func02)


# 注意: 如果func有参数,那么传入的函数也必须有相同参数
def func04(func):
    print("func04执行了")
    # 先用
    func(10)


# func04(func02)
# 后做(满足先用的逻辑)
def func05(p):
    print("func05,参数是:", p)


func04(func05)
