"""
    人为创造异常
        快速传递错误消息
        异常处理完整流程:
          raise .... -->  try except:
            创建             接收
"""

class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 23 <= value <= 30:
            self.__age = value
        else:
            # 创建异常
            # 语法:raise Exception(数据)
            raise Exception("我不要",1001,"if 23 <= value <= 30")


while True:
    # 接收异常
    # 语法:except Exception as e:
    try:
        age = int(input("请输入年龄:"))
        w01 = Wife(age)
        print(w01.age)
        break
    except Exception as e:
        print(e.args)
