"""
    内置生成器
        enumerate
"""
list01 = [4, 4, 5456, 67, 7, 78]
# 从头到尾读取数据
for item in list01:  # 缺点:因为没有索引,所以不能修改
    print(item)

# 非从头到尾读取数据
for i in range(len(list01)):  # 缺点:range思考的要素较多
    print(list01[i])
    # list01[i] = 0

# 同时获取索引与元素
# element 是 元组 (索引,元素)
# for element in enumerate(list01):
#     print(element[0],element[1])
for i, item in enumerate(list01):
    print(i, item)

# 快捷键:iter +  回车
for item in list01:
    print(item)

for i in range(len(list01)):
    print(list01[i])

# 快捷键:itere +  回车
for i, item in enumerate(list01):
    print(i, item)
