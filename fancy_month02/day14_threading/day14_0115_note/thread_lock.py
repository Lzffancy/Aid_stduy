"""
use lock to control thread
"""

from threading import Thread,Lock
from time import sleep
lock =Lock()
a= b= 0

def value():
    while True:

        if a==b:
                print(r"我俩走到一起啦！！a=%db=%d"%(a,b))
                sleep(0.1)
        else:
            print('分手吧a=%db=%d'%(a,b))
        sleep(2)


t = Thread(target=value)
t.start()

while 1:
    lock.acquire()
    a+=1
    b+=1
    lock.release()
