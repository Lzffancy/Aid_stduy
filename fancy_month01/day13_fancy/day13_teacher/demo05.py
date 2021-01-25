"""
    Python程序结构

根目录
    包(文件夹)
        模块(文件)
            类
                函数(方法)
                    语句
"""
# 路径:从根目录开始

# 方式1
# import package01.package02.module02 as m
# m.func01()

# 方式2
# from package01.package02.module02 import func01
from package01.package02.module02 import func01

func01()
# 练习1：
# 1.	根据下列结构，创建包与模块。
# my_project01 /
# main.py
# common/
# __init__.py
# list_helper.py
# skill_system/
#         __init__.py
#         skill_deployer.py
# 	      skill_manager.py
# 2.	在main.py中调用skill_manager.py中实例方法。
# 3.	在skill_manager.py中调用skill_deployer.py中实例方法。
# 4.	在skill_deployer.py中调用list_helper.py中类方法。