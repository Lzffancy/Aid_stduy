"""
threading
"""
import threading
from time import sleep
import os

a=1
def music():
    global a
    a = 10000
    for  i in range(2):
        sleep(2)
        print("thread01,play.得得得的的多多的的")
        print(os.getpid())


def music02():
    for  i in range(4):
        sleep(1)
        print("main,play.啊啊啊那就是黑猫警长！")
        print(os.getpid())


thr = threading.Thread(target=music)
thr.start()
print(os.getpid())
music02()
thr.join()
print('a=',a)