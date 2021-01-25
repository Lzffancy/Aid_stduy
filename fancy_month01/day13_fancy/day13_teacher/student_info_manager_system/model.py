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