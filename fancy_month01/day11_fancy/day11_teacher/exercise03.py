"""
    自定义对象使用运算符
        减法
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self


pos01 = Vector2(3, 2)
pos02 = Vector2(1, 5)
print(id(pos01))
pos01 -= pos02
print(id(pos01))
print(pos01.__dict__)
