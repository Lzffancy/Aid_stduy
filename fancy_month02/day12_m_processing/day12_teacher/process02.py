"""
含有参数的进程函数
"""
from multiprocessing import Process
from time import sleep


# 带有参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")


# 实例化进程对象
# p = Process(target=worker,args=(2,"Tom"))

p = Process(target=worker,
            args = (2,),
            kwargs={"name": "Tom"},
            daemon=True) # 该子进程会随父进程退出
p.start()

sleep(5)

