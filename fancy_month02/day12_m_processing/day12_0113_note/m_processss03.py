'''

'''
from multiprocessing import *
import os, sys
from time import *


def th1():
    sleep(2)
    print('1')
    print(os.getppid(), '-----', os.getpid())


def th2():
    # sys.exit()
    sleep(5)
    print('2')
    print(os.getppid(), '-----', os.getpid())


def th3():
    sleep(2)
    print('3')
    print(os.getppid(), '-----', os.getpid())


jobs = []
for th in [th1, th2, th3]:
    p = Process(target=th)
    jobs.append(p)
    p.start()

# 父进程等待所有子进程
for each_process in jobs:
    each_process.join()
