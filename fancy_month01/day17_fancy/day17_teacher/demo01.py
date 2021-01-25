"""
    笛卡尔积
"""
import itertools

# 2个色子可以组成的可能性哪些
# for x in range(1, 7):
#     for y in range(1, 7):
#         print(x, y)

for item in itertools.product(range(1, 7), range(1, 7)):
    print(item)

# n个色子可以组成的可能性哪些
count = int(input("请输入色子个数:"))
for item in itertools.product(range(1, 7), repeat=count):
    print(item)
