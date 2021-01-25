list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]
list_student_sex = ["男", "男", "女"]

list_student = []


class Student:
  def __init__(self,name,age,sex):
   self.name = name
   self.age = age
   self.sex = sex


for item in zip(list_student_name,list_student_age,list_student_sex):
   #print(item)  #将其ｚｉp为一个个元组
   stu = Student(*item)  #实参加*是拆分实参，放给数据ｍｏｄｅｌ
   list_student.append(stu) #将这样的一个个数据ｍｏｄｅｌ添加到ｌｉｓｔ中
                            #{'name': '悟空', 'age': 28, 'sex': '男'}
   for each in list_student:
    print(each.__dict__)
#这里使用列表推导式
list_student = [Student(*item)
                for item in zip(list_student_name,list_student_age,list_student_sex)]
                #将每个ｚｉｐ好的ｉｔｅｍ元组　拆分（*item）元素放入
                #Student(*item)　进行打包成　对象

for item in list_student:
  print(item,'我是打包好的对象')
  print(item.__dict__)
