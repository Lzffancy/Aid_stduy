"""
    练习2：创建图形管理器
        1. 记录多种图形（圆形、矩形....）
        2. 提供计算总面积的方法.
        满足：
            开闭原则
        测试：
            创建图形管理器，存储多个图形对象。
            通过图形管理器，调用计算总面积方法.
        要求:
            画出架构设计图
            编码.调试(体会多态)
            写出三大特征,设计原则的体现
"""


class GraphicManager:
    def __init__(self):
        self.__all_graphic = []

    def add_graphic(self, graphic):
        if isinstance(graphic,Graphic):
            self.__all_graphic.append(graphic)

    def get_total_area(self):
        total_area = 0
        for item in self.__all_graphic:
            total_area += item.calculate_area()
        return total_area


class Graphic:
    def calculate_area(self):
        pass


# ----------程序员------------
class Rectangle(Graphic):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w


class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2


# ----------入口------------
manager = GraphicManager()
manager.add_graphic(Circle(5))
manager.add_graphic(Rectangle(2, 3))
manager.add_graphic("圆形")
print(manager.get_total_area())
