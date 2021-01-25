"""
    遍历自定义对象
    创建迭代器
"""


class StudentIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]


class StudentController:
    def __init__(self):
        self.__list_students = []

    def add(self, stu):
        self.__list_students.append(stu)

    def __iter__(self):
        return StudentIterator(self.__list_students)


controller = StudentController()
controller.add("苏轩平")
controller.add("德吉卡卓")
controller.add("王磊")
# for item in controller:
#     print(item)  # ?
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
