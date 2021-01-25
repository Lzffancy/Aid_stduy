"""
    创建颜色类,创建颜色列表
    通过内置函数实现以下功能:
        获取颜色最深(r+g+b)的
        查找Color(1,0,1)的数量
        查找Color(1,0,1)的索引 列表.index
"""


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __gt__(self, other):
        return self.r + self.g + self.b > other.r + other.g + other.b

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


list_color = [
    Color(0.1, 0.8, 0.2),
    Color(1, 0, 0.5),
    Color(1, 0, 1),
    Color(0, 1, 1),
]

max_value = max(list_color)
print(max_value.__dict__)

count = list_color.count(Color(1, 0, 1))
print(count)

index = list_color.index(Color(1, 0, 1))
print(index)
