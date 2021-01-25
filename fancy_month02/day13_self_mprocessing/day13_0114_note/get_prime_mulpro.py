"""
多进程处理
多线程间消息列求和
计算时间　装饰器
"""

from multiprocessing import Process,Queue
from time import time
q = Queue()

def time_is(func):
    def warrper(*args,**kwargs):
        s_time = time()
        result =func(*args,**kwargs)
        e_time = time()

        print('runing time:',e_time-s_time)
        return result
    return warrper


class Get_prime(Process):
    def __init__(self, begin, end):
        self.begin =begin
        self.end =end
        super().__init__()
    # 当无需传入参数，又是仅仅在类内使用时候　采用静态方法
    @staticmethod
    def is_prime(x):
        if x<=1:
            return False
        for i in range(2,x//2+1):
            if x % i == 0:
               return False
        return True

    def run(self) -> None:
        prime  =[]
        for i in range(self.begin,self.end):
            if Get_prime.is_prime(i):
                prime.append(i)
        q.put(sum(prime))

@time_is
def process_4():
    result =0
    for i in range(1,100001,25000):
        p = Get_prime(i,i+25000)
        p.start()
        print("进程开始",i)
    for i in range(4):
        result += q.get()
    return result


if __name__ == '__main__':
    result = process_4()
    print(result)