"""

"""


# 任何一个类都直接或者间接继承object
class Car(object):
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    # 对象-转换为->str
    def __str__(self):
        return f"{self.brand}车速是{self.speed}"


# 魔法
# 直接打印自定义对象的格式
# 默认为:<__main__.Car object at 0x7f472100ddd8>
# 重新后:宝马车速是200
c01 = Car("宝马", 200)
print(c01)
# 练习：
#     直接打印商品对象: xx的编号是xx,单价是xx
#     直接打印敌人对象: xx的攻击力是xx,血量是xx
