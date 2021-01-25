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
    """
        集成操作框架
        可迭代对象助手
    """

    @staticmethod
    def find_all(iterable, condition):
        """
            在可迭代对象中,查找满足条件的全部元素
        :param iterable:可迭代对象
        :param condition:函数类型的查找条件
        :return:生成器,推算满足条件的元素
        """
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def find_single(iterable, condition):
        """
            在可迭代对象中,查找满足条件的单个元素
        :param iterable:可迭代对象
        :param condition:函数类型的查找条件
        :return:满足条件的元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def get_count(iterable, condition):
        """
            在可迭代对象中查找满足条件的元素数量
        :param iterable:可迭代对象
        :param condition:查找条件
        :return:数量
        """
        count = 0
        for item in iterable:
            if condition(item):
                count += 1
        return count

    @staticmethod
    def sum(iterable, handle):
        """
            根据指定逻辑,对可迭代对象中的元素进行累加操作
        :param iterable:可迭代对象
        :param handle:累加逻辑
        :return:累加和
        """
        sum_value = 0
        for item in iterable:
            sum_value += handle(item)
        return sum_value

    @staticmethod
    def select(iterable, handle):
        """
            在可迭代对象中,根据指定逻辑搜索内容
        :param iterable:可迭代对象
        :param handle:对每个元素的处理逻辑
        :return:生成器,推算搜索的内容
        """
        for item in iterable:
            yield handle(item)

    @staticmethod
    def delete_all(iterable, condition):
        """
            根据条件删除可迭代对象中的元素
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:删除的数量
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, condition):  # lambda item:item.money
        """
            根据条件在可迭代对象中查找最大值
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:最大值
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            # if max_value.money < iterable[i].money:
            if condition(max_value) < condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def get_min(iterable, condition):
        """
            根据条件在可迭代对象中查找最小值
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:最小值
        """
        min_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(min_value) > condition(iterable[i]):
                min_value = iterable[i]
        return min_value

    @staticmethod
    def ascending_order(iterable, condition):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) > condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    @staticmethod
    def descending_order(iterable, condition):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                # if iterable[r].eid < iterable[c].eid:
                if condition(iterable[r]) < condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    @staticmethod
    def is_repeat(iterable, condition):
        """
            根据条件判断可迭代对象中是否存在重复元素
        :param iterable:可迭代对象
        :param condition:判断条件
        :return:bool类型,是否重复
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                # if iterable[r].eid == iterable[c].eid:
                if condition(iterable[r]) == condition(iterable[c]):
                    return True  # 有重复
        return False  # 没重复

    @staticmethod
    def remove_duplicate(iterable, condition):
        for r in range(len(iterable) - 1):
            for c in range(len(iterable) - 1, r, -1):
                if condition(iterable[r]) == condition(iterable[c]):
                    del iterable[c]
