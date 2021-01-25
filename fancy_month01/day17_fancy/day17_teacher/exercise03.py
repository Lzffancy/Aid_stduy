# 练习:请计算4张扑克牌中组合2张的可能性
import itertools

list_poker = ["红桃3","大王","梅花5","黑桃A"]
for item in itertools.combinations(list_poker, 2):
    print(item)