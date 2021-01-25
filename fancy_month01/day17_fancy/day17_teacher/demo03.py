"""
    组合
        从n个元素中抽出m个元素
"""
# 7 个人 选出3个人
import itertools

list_person = ["男1号", "女1号", "男2号", "男3号", "女2号", "女3号", "男5号"]
for item in itertools.combinations(list_person, 3):
    print(item)



