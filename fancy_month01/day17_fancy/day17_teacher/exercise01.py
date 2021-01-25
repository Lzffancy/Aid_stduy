# 练习1:请排列出在3男,4女中,选出2个人的所有可能性
import itertools

list_man = ["男1号", "男2号", "男2号"]
list_woman = ["女1号", "女2号", "女3号", "女4号"]
for item in itertools.product(list_man,list_woman):
    print(item)