"""
    导入
"""
# 备注:如果需要有智能提示,需要标记项目根目录
# 在根目录上右键Mark Directory -> Sources Root

# 1. "我过去"
# 本质:创建变量,存储模块地址
# 语法:import 模块名
# 使用:模块名.成员
# import module01
#
# module01.func01()

# 2. "你过来"
# 本质:目标模块的成员进入当前模块的作用域中
# 语法:from 模块 import 成员
# 使用:直接使用成员
# 注意:命名冲突
# from module01 import func01
# from module01 import func02
from module01 import *

# def func01():
#     print("demo02 -- func01")

func01()
func02()
