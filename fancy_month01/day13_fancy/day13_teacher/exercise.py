"""

"""
# 方式1:更适合面向过程(全局变量,函数)
import module_exercise

print(module_exercise.data)
module_exercise.func01()
# 通过对象调用实例方法
m01 = module_exercise.MyClass()
m01.func02()
# 通过类调用类方法
module_exercise.MyClass.func03()

# 方式2:更适合面向对象(类)
# from module_exercise import data
# from module_exercise import func01
# from module_exercise import MyClass
from module_exercise import *

print(data)
func01()
m02 = MyClass()
m02.func02()
MyClass.func03()
