"""
    yield
"""


class StudentController:
    def __init__(self):
        self.__list_students = []

    def add(self, stu):
        self.__list_students.append(stu)

    # def __iter__(self):
    # 生成迭代器代码的大致规则:
    # 1. 将yield关键字以前的代码存入__next__函数体
    # 2. 将yield关键字以后的数据作为__next__函数返回值
    # index = 0
    # yield self.__list_students[index]
    #
    # index+=1
    # yield self.__list_students[index]
    #
    # index+=1
    # yield self.__list_students[index]

    def __iter__(self):
        for item in self.__list_students:
            yield item


controller = StudentController()
controller.add("苏轩平")
controller.add("德吉卡卓")
controller.add("王磊")
for item in controller:
    print(item)  # ?
# iterator = controller.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
