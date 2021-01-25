"""
    内置生成器
        zip
"""
list01 = [1, 2, 3]
list02 = [4, 5, 6]
# 将多个可迭代对象的对应元素合并为元组
for item in zip(list01, list02):
    print(item)

map = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# 缺点:map的行数不能变化
# for item in zip(map[0], map[1],map[2]):
#     print(item)
# 缺点:没有形成二维列表
# for item in zip(*map):
#     print(list(item))
# 　缺点:创建过于繁琐
# map_new = []
# for item in zip(*map):
#     map_new.append(list(item))

map_new = [list(item) for item in zip(*map)]
print(map_new)
