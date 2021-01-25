"""
    迭代Iteration:重复获取下一个元素的过程
    可迭代对象Iterable:能够参与迭代的对象
        具有__iter__函数
    迭代器Iterator:执行迭代过程的对象
        具有__next__函数

"""
message = "我是齐天大圣孙悟空"
# for item in message:
#     print(item)

# for 原理 - 迭代过程
# 1. 获取迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
    # 3. 如果停止迭代,则跳出循环
    except StopIteration:
        break
# 面试题:能够被for循环的对象,必须具备什么条件?
# 答:对象必须具备__iter__函数(必须是可迭代对象)

