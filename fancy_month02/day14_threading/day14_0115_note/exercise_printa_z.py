"""
线程　a-z 13-39  65-91
"""
from threading import Thread,Lock
result=[]
lock01 = Lock()
lock02 = Lock()
#用加锁　阻塞　来保证每个线程都不能连续执行
def yeid_num():
    for num in range(1,53,2):
        lock01.acquire()
        print('%d%d'%(num,num+1))
        lock02.release()

def yeid_echr():
    for echr in range(65,91):
        lock02.acquire()
        print(chr(echr))
        lock01.release()

thr_num =Thread(target=yeid_num)
thr_echr =Thread(target=yeid_echr)

lock02.acquire()

thr_num.start()
thr_echr.start()


if __name__ == '__main__':

 pass


