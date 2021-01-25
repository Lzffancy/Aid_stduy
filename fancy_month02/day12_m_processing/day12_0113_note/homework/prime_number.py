"""
"""
import time
from multiprocessing import *


def time_counter(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("用时", end_time - start_time)
    return wrapper


@time_counter
def get_primer_number(start_num=2, final_num=0,p='p0'):
    sum = 0
    for i in range(start_num, final_num + 1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            # print(i)
            sum += i
    # common_sum.appent(sum)
    print("质数之和", sum,p)
    with open('result.txt',"a") as file:
         file.write("%s "%sum)
    return sum


if __name__ == '__main__':
    #get_primer_number(2,100000)


    "启用多进程"
    start_time = time.time()
    p1 = Process(target=get_primer_number,args=(2,25000,'p1'))
    p2 = Process(target=get_primer_number, args=(25001, 72000,'p2'))
    p3 = Process(target=get_primer_number, args=(72001, 75000,'p3'))
    p4 = Process(target=get_primer_number, args=(75001, 100000,'p4'))

    for sth in [p1,p2,p3,p4]:
        print("计算中",sth)
        sth.start()
        #sth.join()
        #print("计算结束", sth)
    [sth.join() for sth in [p1,p2,p3,p4]]
    end_time = time.time()
    print('多进程用时',end_time-start_time)
    # p1.start()
    # print(p1)
