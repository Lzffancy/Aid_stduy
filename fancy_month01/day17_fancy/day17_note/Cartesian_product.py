import itertools
# 3男　４女　,两人组合
['男１','男2','男3']
['女１','女2','女3','女4']
count = 0
for item in itertools.product(['男１','男2','男3'],['女１','女2','女3','女4']):
    print(item)
    count += 1
print('有%d种'%count)