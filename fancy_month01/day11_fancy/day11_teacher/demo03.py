"""
    +=
"""


class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # +:返回新数据
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    # +=:返回旧数据
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

pos01 = Vector2(2, 1)
pos02 = Vector2(3, 2)
pos01 += pos02
print(pos01.__dict__)

# 对于可变对象,+=在原有基础上修改
list01 = [1]
print(id(list01))# 139748736970504
list01 += [2]
print(id(list01))# 139748736970504
# 对于不可变对象,+=创建新数据
tuple01 = (1,)
print(id(tuple01))# 139748767411224
tuple01 += (2,)
print(id(tuple01))# 139748736959304