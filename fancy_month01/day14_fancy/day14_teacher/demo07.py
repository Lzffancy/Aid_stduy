"""
    生成器应用
        函数返回多个结果,不用容器存储.
        使用yield返回.

        备注:函数有一个结果,使用return返回
"""


# 需求:创建函数,生成器1--10之间能被3整除的数字
# 传统思想:创建容器存储所有结果
def get_number01():
    list_result = []
    for number in range(1, 11):
        if number % 3 == 0:
            list_result.append(number)
    return list_result


res = get_number01()
for item in res:
    print(item)


def get_number02():
    for number in range(1, 11):
        if number % 3 == 0:
            yield number


res = get_number02()
for item in res:
    print(item)
