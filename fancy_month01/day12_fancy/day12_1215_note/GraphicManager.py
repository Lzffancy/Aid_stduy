#
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
import math
class Graphic_Manager:
    def __init__(self):
        self.__all_graph = []         # 类中的　私有的all graph
    def add_graph(self,graph):     #　管理器的功能
        if isinstance(graph,Graphs):
         self.__all_graph.append(graph)
        else:
            print("无此子类",graph)
            pass
        #１．继承Ｇｒａｐｈｓ,调用子方法
    def get_total_area(self):
        total_area = 0#　新建变量
        for each in self.__all_graph:
            total_area += each.calulate_area()#架构先想到的需要实现的需求
        return total_area

#-----------------------------------父（参照）
class Graphs:
    def calulate_area(self):
        pass
#-----------------------------------
class Circle(Graphs):
    def __init__(self,r):
        self.r = r
    def calulate_area(self):#２．重写父类中安排的方法
        return self.r*self.r*3.14

class Rectangel(Graphs):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def calulate_area(self):
        return self.l * self.w

#------------入口-----------------
pic_manager = Graphic_Manager()
pic_manager.add_graph(Circle(1))#３．+创建子类图形
pic_manager.add_graph(Rectangel(1,1))
pic_manager.add_graph('fancy')
print(pic_manager.get_total_area())

'''三大特征
　　封装：　创建　管理器和　圆形　矩形类
　　继承：　创建图形父类，并隔离　图形管理器和　具体图形（圆、矩）
　　多态：　具体图形　的不同面积计算方法

设计原则
　　开闭：　增加新图形不影响管理器类
　　单一：　
　　　　　　管理器类负责　增加　储存　计算总面积
　　　　　　圆　负责　创建圆　计算圆形面积
　　　　　　矩　负责　创建矩　计算矩面积
　　依赖抽象: 
　　　　　　管理器类直接调用　图形类　不用管具体图形
　　组合复用：
　　　　　　管理器和　具体图形　属于组合
　　　　　　图形和　具体图形　属于继承'''