class Iterable_tool:
    @staticmethod                  #不接收实例变量和类变量,他要函数　做为变量
    def find_all(iterable, condition):
        for number in iterable:
            if  condition(number):
                # print(number._dict_)
                yield number
    @staticmethod
    def find_single(iterable,condition):
        for item in iterable:
            if condition(item):
               return item

    @staticmethod
    def get_count(iterable,condition):
        count = 0
        for item in iterable:
            if condition(item):   #与参数构造调用函数
                count += 1
        return count

    @staticmethod                  #不自动传参数
    def sum_all(iterable,lambdax):
        sum_count = 0
        for item in iterable:
                sum_count += lambdax(item)
        return sum_count

    @staticmethod
    def select(iterable,lambdax):
        '''
        按照lambdax逻辑在iterable中搜索并返回列表
        '''
        selec_list = []
        for each in iterable:
            selec_list.append(lambdax(each))
        return selec_list

    @staticmethod
    def delete_all(iterable,lambdax):
        '''
    　　　照lambdax逻辑在iterable　删除
    　　　并返回删除次数
        '''
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if lambdax(iterable[i]):    #item: item.did == 9002
               del iterable[i]          #    iterable[i].did
               count += 1
        return count

    @staticmethod
    def get_max(iterable,lambdax):
        """
        """
        max_value = iterable[0]
        for i in range(1,len(iterable)):
            if lambdax(max_value) < lambdax(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def descending(iterable, lambdax):
        for r in range(len(iterable)-1):#取数据,先取得第一个
            for c in range(r + 1, len(iterable)):#做比较，历遍第一个之后的其他个
                if lambdax(iterable[r]) < lambdax(iterable[c]):#发现更大
                    iterable[r], iterable[c] = iterable[c], iterable[r]#做交换

    @staticmethod
    def is_reapt(iterable, lambdax):
        for r in range(len(iterable) - 1):  # 取数据
            for c in range(r + 1, len(iterable)):  # 做比较
                if lambdax(iterable[r]) == lambdax(iterable[c]):
                    return True
        return False                      #全部循环完成才退出　并返回Ｆalse

    @staticmethod
    def remove_duplicate():
        pass  #????????????????????????????????????????
