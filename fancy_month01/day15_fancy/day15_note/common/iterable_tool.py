class Iterable_tool:
    @staticmethod                  #不接收实例变量和类变量
    def find_all(iterable, condition):
        for number in iterable:
            if not condition(number):
                # print(number._dict_)
                yield number
    @staticmethod
    def find_single(iterable,condition,number):
        for item in iterable:
            if condition(item,number):
                yield item

    @staticmethod
    def get_count(iterable,condition,number):
        count = 0
        for item in iterable:
            if condition(item,number):   #与参数构造调用函数
                count += 1
        return number,count