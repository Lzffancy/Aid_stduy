"""
3. 需求：
    定义函数,在商品列表中获取单价最小商品
    定义函数,在商品列表中获取编号最小商品
   步骤：
    1. 根据需求，写出函数。
    2. 因为主体逻辑相同,核心算法不同.
    3. 在IterableHelper中创建函数get_min

4. 需求：
    定义函数,在商品列表中根据单价对商品列表进行升序排列
    定义函数,在商品列表中根据单价对商品列表进行升序排列
   步骤：
    1. 根据需求，写出函数。
    2. 因为主体逻辑相同,核心算法不同.
    3. 在IterableHelper中创建函数ascending_order
"""
from common.iterable_tools import IterableHelper


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

"""
def get_min01():
    min_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if min_value.price > list_commodity_infos[i].price:
            min_value = list_commodity_infos[i]
    return min_value

def get_min02():
    min_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if min_value.cid > list_commodity_infos[i].cid:
            min_value = list_commodity_infos[i]
    return min_value

def condition01(com):
    return com.cid

def condition02(com):
    return com.price

def get_min(condition):
    min_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        # if min_value.cid > list_commodity_infos[i].cid:
        # if condition01(min_value) > condition01(list_commodity_infos[i]):
        # if condition02(min_value) > condition02(list_commodity_infos[i]):
        if condition(min_value) > condition(list_commodity_infos[i]):
            min_value = list_commodity_infos[i]
    return min_value
"""

min_value = IterableHelper.get_min(list_commodity_infos, lambda com: com.price)
print(min_value.__dict__)

"""
def ascending_order01():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price > list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]

def ascending_order02():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].cid > list_commodity_infos[c].cid:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


def ascending_order(condition):
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            # if list_commodity_infos[r].price > list_commodity_infos[c].price:
            if condition(list_commodity_infos[r]) > condition(list_commodity_infos[c]):
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
"""

IterableHelper.ascending_order(list_commodity_infos, lambda item: item.price)

for item in list_commodity_infos:
    print(item.__dict__)
