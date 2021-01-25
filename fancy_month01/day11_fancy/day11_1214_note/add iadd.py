
class Vector2:
    """
        二维向量
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
#
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
    def __sub__(self, other):
        # 向量与向量相减
        if type(other) == Vector2:
            x = self.x - other.x
            y = self.y - other.y
        # 向量与数字相减
        elif type(other) in (int, float):
            x = self.x - other
            y = self.y - other
        return Vector2(x, y)
    def __mul__(self, other):
        if type(other) == Vector2:
            x = self.x * other.x
            y = self.y * other.y
        elif type(other) in (int, float):
            x = self.x * other
            y = self.y * other
        return Vector2(x, y)

#　返回自己　return self
    def __isub__(self, other):
        if type(other) == Vector2:
             self.x -= other.x
             self.y -= other.y
        elif type(other) in (int, float):
             self.x -= other
             self.y -= other
        return self
# 自定义print
    def __str__(self):
        return "(%d,%d)" %(self.x,self.y)
# 重载比较运算
    def __eq__(self,other):
       pass
    def __gt__(self, other):
       pass

# 基本自定义　add sub mul  结果会新建对象
pos01 = Vector2(2, 1)
pos02 = Vector2(3, 2)
pos03 = pos01 - pos02  # pos01.__add__(pos02)
print(pos03.__dict__)

pos04 = pos01 * 5
print(pos04)

# 自减地址相同　return self
pos04 -= 1
print(pos04,id(pos04))
pos04 -= 1
print(pos04,id(pos04))