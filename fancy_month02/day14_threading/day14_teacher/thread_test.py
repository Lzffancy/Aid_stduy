from threading import Thread
from time import time

def timeis(func):
    def wrapper(*args,**kwargs):
        start_time = time()
        res = func(*args,**kwargs)
        end_time = time()
        print("执行时间:",end_time - start_time)
        return res
    return wrapper

class Prime(Thread):
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

@timeis
def process_10():
    jobs = []
    for i in range(1,100001,10000):
        t = Prime(i,i + 10000)
        jobs.append(t)
        t.start()
    for i in jobs:
        i.join()


if __name__ == '__main__':
    process_10()