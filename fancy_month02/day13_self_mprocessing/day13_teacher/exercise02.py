from multiprocessing import Process,Queue
from time import time

q = Queue() # 消息队列

def timeis(func):
    def wrapper(*args,**kwargs):
        start_time = time()
        res = func(*args,**kwargs)
        end_time = time()
        print("执行时间:",end_time - start_time)
        return res
    return wrapper

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
        q.put(sum(prime)) # 存入结果

@timeis
def process_10():
    result = 0
    for i in range(1,100001,10000):
        p = Prime(i,i + 10000)
        p.start()
    for i in range(10):
        result += q.get() #获取每个进程的最后结果
    return result

if __name__ == '__main__':
    # 执行时间: 7.4214277267456055
    # 执行时间: 6.722904920578003
    result = process_10()
    print(result)