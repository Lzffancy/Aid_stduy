'''
带参线程
'''

from threading import Thread
from time import sleep


def func01(sec,name):
    print('func01含有参数的线程')
    sleep(sec)
    print('%s 线程执行完毕'%name)



for i in range(5):
    t = Thread(target=func01,
               args=(2,),
               kwargs={'name':'t-%d'%i},
               daemon=True)
    t.start()

