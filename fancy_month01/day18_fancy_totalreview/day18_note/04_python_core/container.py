"""
四.运算符
    身份运算符is: 判断两个变量存储的数据是否为同一个
五.容器
        特点:
            字符串:存储字符编码,不可变,序列
            列表:存储变量,可变,序列
            元组:存储变量,不可变,序列
            字典:存储键值对,可变,散列
                键:唯一且不可变数据
            集合:存储键,可变,散列
        类型转换:
            列表 = list( 可迭代对象 )
            元组 = tuple( 可迭代对象 )
            # 格式:
            字典 = dict( 可迭代对象 )
"""
a = 10
b = a  # 10的引用计数为2
del a, b

c = 50
c = 60

list01 = []
list02 = []
list01.append(list02)
list02.append(list01)

# str_result = ""
# for number in range(10):
#     # str_result += str(number)
#     str_result = str_result + str(number)
# print(str_result)

# 频繁修改:用可变对象,代替不可变对象.
list_result = []
for number in range(10):
    list_result.append(str(number))
print(list_result)

# 对象池(内置对象池:字符串池.整数迟,小数池,bool池):
# 当数据创建时,会判断池中是否具有相同成员
# 如果没有,开辟空间创建新数据
# 如果有,直接返回数据地址,不再创建新数据.
# 优点:提高内存利用率
data01 = 10
data02 = 10
print(id(data01))
print(id(data02))

# True 表示是同一对象
# False 表示不是同一对象
print(data01 is data02)

list01 = [10]
list02 = list01
print(list01 is list02)  # True

# 列表元素必须能够一分为二
list01 = ["aA", ("b", "B"), ["c", "C"]]
dict01 = dict(list01)  # {'a': 'A', 'b': 'B', 'c': 'C'}
print(dict01)
# 列表存储的是key
list02 = list(dict01)
print(list02)  # ['a', 'b', 'c']
# 列表存储的是key和value
list02 = list(dict01.items())  #dict ---> list[tuple()]
print(list02)  # [('a', 'A'), ('b', 'B'), ('c', 'C')]

list03 = [1, 2, 3]
list04 = list(list03) # list03[:] 浅拷贝
list03[0] = 10
print(list04[0]) # 1