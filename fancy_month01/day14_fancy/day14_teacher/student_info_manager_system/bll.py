from model import StudentModel


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

# 测试
if __name__ == '__main__':
    # 当前模块是主模块才执行(测试环境)
    # 当前模块被导入时不执行(真实环境)
    controller = StudentController()
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
    for item in controller.list_students:
        print(item)