"""

"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # 向量与向量相加
        if type(other) == Vector2:
            x = self.x + other.x
            y = self.y + other.y
        # 向量与数字相加
        elif type(other) in (int, float):
            x = self.x + other
            y = self.y + other
        return Vector2(x, y)

pos01 = Vector2(2, 1)
pos02 = Vector2(3, 2)
pos03 = pos01 + pos02  # pos01.__add__(pos02)
print(pos03.__dict__)

pos04 = pos01 + 5
print(pos04.__dict__)
