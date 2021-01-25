"""
    可迭代对象工具
"""


class IterableHelper:
    """
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
    def find_single(iterable,condition):
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
    def get_count(iterable,condition):
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

