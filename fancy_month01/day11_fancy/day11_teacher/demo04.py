"""
    比较运算符重载
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 判断两个对象是否相同的依据
    def __eq__(self, other):
        return self.x == other.x and self.y == self.y

    # 判断两个对象大小的依据
    def __gt__(self, other):
        return self.x ** 2 + self.y ** 2 >other.x ** 2 + other.y ** 2


pos01 = Vector2(1, 1)
pos02 = Vector2(1, 1)
# 重写__eq__实现
# 默认比较数据的内存地址 False
# 重写eq后可以自定义比较规则
print(pos01 == pos02)
list_position = [
    Vector2(1, 1),
    Vector2(5, 5),
    Vector2(2, 2),
    Vector2(4, 4),
    Vector2(3, 3),
]
print(pos01 in list_position)
print(list_position.count(pos01))
# ...
# 重写__gt__实现
print(pos01 > pos02)
max_value = max(list_position)
print(max_value.__dict__)

print(min(list_position).__dict__)
