"""
    1.将find_all函数,定义到common/iterable_tools模块中
    2.将函数修改为静态方法
    3.在当前模块中调用,实现查找奇数
    4.再实现查找能被2,5整除的数字
"""
from common.iterable_tools import IterableHelper

list01 = [4, 354, 65, 7, 78]


def condition01(item):
    return item % 2


def condition02(data):
    return data % 2 == 0 or data % 5 == 0


for item in IterableHelper.find_all(list01, condition01):
    print(item)

for item in IterableHelper.find_all(list01, condition02):
    print(item)
