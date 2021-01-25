"""
    学生信息管理系统

    练习:商品信息管理系统
        1. 添加商品信息.
        2. 存储商品信息.
        3. 显示商品信息
        4. 删除商品信息
        5. 修改商品信息
"""


class StudentModel:
    """
        学生信息模型
    """

    def __init__(self, name="", sex="", score=0, age=0, sid=0):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age
        # 全球唯一标识符(系统决定)
        self.sid = sid

    def __str__(self):
        return str(self.__dict__)


class StudentView:
    """
        学生视图:负责处理界面逻辑
    """

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            # 生成函数快捷键:atl + 回车
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        stu.sex = input("请输入学生性别:")
        stu.score = int(input("请输入学生成绩:"))
        stu.age = int(input("请输入学生年龄:"))
        self.__controller.add_student(stu)
        print("添加成功")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_students(self):
        for item in self.__controller.list_students:
            # 需要重写学生类的__str__方法
            print(item)

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号:"))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入学生编号:"))
        stu.name = input("请输入学生姓名:")
        stu.sex = input("请输入学生性别:")
        stu.score = int(input("请输入学生成绩:"))
        stu.age = int(input("请输入学生年龄:"))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")


class StudentController:
    def __init__(self):
        self.__list_students = []
        self.__start_id = 1001

    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, target):
        """
            添加学生信息
        :param target:
        """
        target.sid = self.__start_id
        self.__start_id += 1
        self.__list_students.append(target)

    def remove_student(self, sid):
        """
            移除学生信息
        :param sid:学生编号
        :return:是否移除成功
        """
        for i in range(len(self.__list_students)):
            if self.__list_students[i].sid == sid:
                del self.__list_students[i]
                return True  # 删除成功
        return False  # 删除失败

    def update_student(self, stu):
        """
            修改学生信息
        :param stu:需要修改的信息
        :return:是否修改成功
        """
        for item in self.__list_students:
            if item.sid == stu.sid:
                # item.name = stu.name
                # item.age = stu.age
                item.__dict__ = stu.__dict__
                return True
        return False


# 入口
view = StudentView()
view.main()
