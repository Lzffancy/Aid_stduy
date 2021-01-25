




from comm_helper_tool.commodity_tool import IterableHelper


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
#草稿1
# def condition(item):
#     return item.price
#
# def get_min():
#     min_vlue = list_commodity_infos[0].price
#     min_index = 0
#     for i in range(1,len(list_commodity_infos)):
#         if list_commodity_infos[i].price < min_vlue:
#             min_vlue = list_commodity_infos[i].price
#             min_index = i
#     return min_vlue,list_commodity_infos[min_index]


low_price = IterableHelper.get_min(list_commodity_infos,lambda item :item.price)
print(low_price)
low_cid= IterableHelper.get_min(list_commodity_infos,lambda item :item.cid)
print(low_cid)
#草稿2
# def ascending_order():
#     for r in range(len(list_commodity_infos)-1):
#       print(r)
#       for c in range(r+1,len(list_commodity_infos)):
#          if list_commodity_infos[r].price < list_commodity_infos[c].price:
#             continue
#          else:
#              list_commodity_infos[r],list_commodity_infos[c]  = list_commodity_infos[c],list_commodity_infos[r]
#
#
# ascending_order()
# for each in list_commodity_infos:
#     print(each.__dict__)
# #
#
# a= 1
# b = 2
#
# t = a
# a = b
# b = t
#
# print(a,b)

IterableHelper.ascending_order(list_commodity_infos,lambda item:item.price)

for each in list_commodity_infos:
    print(each.__dict__)

for item in map(lambda item:(item.name,item.price),list_commodity_infos):
    print(item,'name')

for item in filter(lambda item: item.price <1000,list_commodity_infos):
    print(item.__dict__,'object')

res = sorted(list_commodity_infos,key=lambda item : item.price,reverse=True)
for item in res:
    print(item.__dict__)

# 4. ([1,1],[2,2,2],[3,3,3])
#    获取元组中长度最大的列表
tuple01 = ([1, 1], [2, 2, 2], [3, 3, 3])
print(max(tuple01, key=lambda item: len(item)))
