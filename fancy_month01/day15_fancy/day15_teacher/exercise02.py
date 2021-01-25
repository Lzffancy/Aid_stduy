"""
    # 练习：使用学生列表封装以下三个列表中数据
    # list_student_name = ["悟空", "八戒", "白骨精"]
    # list_student_age = [28, 25, 36]
    # list_student_sex = ["男", "男", "女"]
    #
    # list_student = [
    #    Student("悟空",28, "男")
    # ]
"""


class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]
list_student_sex = ["男", "男", "女"]

list_student = []
for item in zip(list_student_name, list_student_age, list_student_sex):
    # print(item)
    # stu = Student(item[0], item[1], item[2])
    stu = Student(*item)
    list_student.append(stu)

list_student = [Student(*item) for item in zip(list_student_name, list_student_age, list_student_sex)]
for item in list_student:
    print(item.__dict__)
