"""
编写一个自定义的进程类，传入两个数据，获取这两个数值
之间的质数之和
"""
from multiprocessing import Process

class Prime(Process):
    # 判断一个数是否为质数
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2,n // 2 + 1):
            if n % i == 0:
                return False
        return True

    def __init__(self,begin,end):
        self.__begin = begin
        self.__end = end
        super().__init__()

    def run(self):
        prime = [] # 存放所有质数
        for i in range(self.__begin,self.__end):
            if Prime.is_prime(i):
                prime.append(i)
        print(sum(prime))

if __name__ == '__main__':
    p = Prime(1,10001)
    p.start()