"""
    函数式编程思想:
        解决的问题:
            多个函数,主体逻辑相同,核心算法不同
        思想:
            "封装"分:将不同的核心算法单独定义到函数中,
                    将主体逻辑也定义到单独函数中
            "继承"隔:使用参数在主体逻辑函数中隔离不同的核心算法函数
            "多态"做:将来再增加新的核心算法,
                    只需要按照在主体逻辑函数中使用参数的规则定义新函数
"""
list01 = [454, 56, 7, 78, 89]

"""
# 需求1:定义函数,在列表中查找所有大于10的数字
def find_all01():
    for item in list01:
        if item > 10:
            yield item

# 需求2:定义函数,在列表中查找所有小于100的数字
def find_all02():
    for item in list01:
        if item < 100:
            yield item

for item in find_all01():
    print(item) 
"""

# 分 - 变化的代码
def condition01(item):
    return item > 10

def condition02(item):
    return item < 100

# find_all 相当于老张
# condition 相当于交通工具
# condition01 相当于火车
# condition02 相当于汽车
# condition....  相当于...
# 分 - 不变的代码
def find_all(condition): # 隔离
    for item in list01:
        # if item < 100:
        # if condition02(item):
        # if condition01(item):
        # 先用
        if condition(item):
            yield item
# 后做
def condition03(item):
    return item % 2 == 0

for item in find_all( condition01 ):
    print(item)

for item in find_all( condition02 ):
    print(item)

for item in find_all( condition03 ):
    print(item)
