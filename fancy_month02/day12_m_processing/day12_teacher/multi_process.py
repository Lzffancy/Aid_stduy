"""
创建多个子进程示例
"""
from multiprocessing import Process
from time import sleep
import os, sys

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),"---",os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),"---",os.getpid())

def th3():
    sys.exit("退出喽")
    sleep(4)
    print("打豆豆")
    print(os.getppid(),"---",os.getpid())

# 循环创建进程
jobs = [] # 装子进程对象
for th in [th1,th2,th3]:
    p = Process(target=th)
    jobs.append(p)
    p.start()

# for结束则表示所有子进程结束
for i in jobs:
    i.join()
