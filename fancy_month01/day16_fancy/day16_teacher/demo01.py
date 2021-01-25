"""
    lambda 表达式
        定义
            匿名函数

        与def函数对比
            匿名函数可以完成的任务def函数都能完成
            lambda语句不支持赋值
            lambda 函数体只能有一句话
"""

# 1. 有参数,有返回值
# def func01(p1, p2):
#     return p1 > p2
#
#
# print(func01(1, 2))

func01 = lambda p1, p2: p1 > p2

print(func01(1, 2))

# 2. 有参数,无返回值
# def func02(p1):
#     print("func02执行了,参数是:", p1)

func02 = lambda p1: print("func02执行了,参数是:", p1)

func02(100)

# 3. 无参数,有返回值
# def func03():
#     return 200
#
# print(func03())

func03 = lambda: 200
print(func03())

# 4. 无参数,无返回值
# def func04():
#     print("func04执行了")
#
# func04()

func04 = lambda: print("func04执行了")

func04()


# 5. 注意1:lambda语句不支持赋值
# def func05(p1):
#     p1[0] = 1000
#
# list01 = [10]
# func05(list01)
# print(list01)# [1000]

# lambda p1:p1[0] = 1000

# 6. 注意2:lambda 函数体只能有一句话
def func06():
    for i in range(5):
        print(i)

func06()

# lambda :for i in range(5): print(i)

