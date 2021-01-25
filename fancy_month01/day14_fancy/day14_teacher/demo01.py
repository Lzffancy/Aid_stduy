"""
    异常处理
        核心价值:让程序按照既定流程执行
        原则:就近处理
"""


# 异常(语法错误)
# print(data) # NameError

# print("1" + 1)  # TypeError

class MyClass:
    pass


m01 = MyClass()


# print(m01.data) # AttributeError

# 异常(逻辑错误:运行时由于数据超过有效范围而引起的异常)
# 方式一(民间喜好):包治百病,处理所有异常
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))# ValueError
        result = apple_count / person_count # ZeroDivisionError
        print("每人%d个苹果"%result)
    # except Exception:
    except:
        print("分苹果失败")

# 方式二(官方建议):对症下药,不同异常不同处理手段
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))  # ValueError
#         result = apple_count / person_count  # ZeroDivisionError
#         print("每人%d个苹果" % result)
#     except ValueError:
#         print("输入的是非整数")
#     except ZeroDivisionError:
#         print("输入的是零")

# 方式三(else):针对没有异常的处理逻辑
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))# ValueError
#         result = apple_count / person_count # ZeroDivisionError
#         print("每人%d个苹果"%result)
#     except Exception:
#         print("分苹果失败")
#     else:
#         print("分苹果成功")

# 方式四(finally):无论对错,一定执行的逻辑
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))  # ValueError
#         result = apple_count / person_count  # ZeroDivisionError
#         print("每人%d个苹果" % result)
#         # 1. 打开文件
#         # 2. 处理文件
#     finally:
#         # 3. 关闭文件
#         print("分苹果结束")


div_apple(10)

print("后续逻辑")
