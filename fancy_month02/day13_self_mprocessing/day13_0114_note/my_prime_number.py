"""
自定义进程
"""
from multiprocessing import *


class PrimeProcess(Process):
    def __init__(self, start_num=2, final_num=0):
        self.start_num = start_num
        self. final_num =  final_num

        # super　同时继承父类的实例变量
        super().__init__()

    def run(self) -> None:
        sum = 0
        for i in range(self.start_num, self.final_num + 1):
            flag = 0
            for j in range(2, i):
                if i % j == 0:
                    flag = 1
                    break
            if flag == 0:
                # print(i)
                sum += i
        # common_sum.appent(sum)
        print("质数之和", sum)
        # with open('result.txt', "a") as file:
        #     file.write("%s " % sum)
        #return sum


if __name__ == '__main__':
    p1 = PrimeProcess(1,10000)
    p1.start()
