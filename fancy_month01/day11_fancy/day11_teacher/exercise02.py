"""
    自定义对象使用运算符
        减法
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if type(other) == Vector2:
            x = self.x - other.x
            y = self.y - other.y
        elif type(other) in (int, float):
            x = self.x - other
            y = self.y - other
        return Vector2(x, y)


pos01 = Vector2(3, 2)
pos02 = Vector2(1, 5)
pos03 = pos01 - pos02
pos04 = pos01 - 2
print(pos04.__dict__)
