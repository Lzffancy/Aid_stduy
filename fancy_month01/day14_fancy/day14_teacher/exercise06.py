"""
    练习3：创建自定义range类，实现下列效果.
    class MyRange:
        pass

    for number in MyRange(5):
        print(number)# 0 1 2 3 4
"""


class MyRangeIterator:  # 迭代器
    def __init__(self, stop):
        self.__count = -1
        self.__stop = stop

    def __next__(self):
        if self.__count >= self.__stop - 1:
            raise StopIteration()
        self.__count += 1
        return self.__count


class MyRange:  # 可迭代对象
    def __init__(self, end):
        self.__end = end

    def __iter__(self):
        return MyRangeIterator(self.__end)


# 循环一次  计算一次  返回一次
for number in MyRange(5):
    print(number)  # 0 1 2 3 4

iterator = MyRange(5).__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
