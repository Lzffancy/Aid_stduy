"""
    yield --> 生成器
"""


# class MyRange:
#     def __init__(self, end):
#         self.__end = end
#
#     def __iter__(self):
#         count = 0
#         while count < self.__end:
#             yield count
#             count += 1

"""
class generator:# 生成器 = 可迭代对象 +  迭代器
    def __iter__(self):
        return self
        
    def __next__(self):
        return ....
"""

def my_range(end):
    count = 0
    while count < end:
        yield count
        count += 1


# for number in my_range(9999999999999999999):
#     print(number)

# print(my_range(5)) # 不执行函数

m01 = my_range(5)
iterator = m01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
