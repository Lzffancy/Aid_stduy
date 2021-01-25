'集成操作框架'
"""
    可迭代对象工具
        价值:
            1. 学习角度:体会函数式编程思想
                三大编程范式
                    面向过程:考虑问题从步骤出发(具体做法)
                        适用性:方法/函数内部实现
                    面向对象:考虑问题从对象出发(谁?干嘛?)
                        适用性:设计软件框架结构
                    函数式编程:将函数作为参数,或者返回值
                        适用性:将具体功能设计灵活
                        查找:工资大于1w,单价小于500,...
                目标:开闭原则(灵活化)
                    分
                    隔
                    做
            2. 实战角度
                自定义高阶函数还可以随着时间推移,不断壮大.
                性能不如内置高阶函数高(优先)
            3. 面试角度
                步骤：
                1. 根据需求，写出函数。
                2. 因为主体逻辑相同,核心算法不同.(分隔做)
                3. 在IterableHelper中创建函数
                (思想来源于微软Linq语言集成查询框架)
"""



class IterableHelper:
    @staticmethod
    def get_min(iterable,condition):
        min_vlue = condition(iterable[0])
        min_index = 0
        for i in range(1, len(iterable)):
            if condition(iterable[i]) < min_vlue:
                min_vlue = condition(iterable[i])
                min_index = i
        return min_vlue, iterable[min_index]


    @staticmethod
    def ascending_order(iterable,condition):
        for r in range(len(iterable)-1):
          #print(r)
          for c in range(r+1,len(iterable)):
             if condition(iterable[r])< condition(iterable[c]):
                continue
             else:
                 iterable[r],iterable[c] = iterable[c],iterable[r]