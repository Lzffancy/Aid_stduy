"""
    将通用代码定义到公共模块中
"""
from common.iterable_tools import IterableHelper

list01 = [454, 56, 7, 78, 89]


def condition01(item):
    return item > 10


def condition02(item):
    return item > 50


for item in IterableHelper.find_all(list01, condition01):
    print(item)

for item in IterableHelper.find_all(list01, condition02):
    print(item)
