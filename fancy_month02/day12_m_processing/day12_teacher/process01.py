"""
创建进程 演示
"""
import multiprocessing as mp
from time import sleep

a = 1 # 全局变量

# 进程执行函数
def fun():
    print("开始运行一个进程喽")
    sleep(4)
    global a
    print("a = ",a)
    a = 10000
    print("进程运行结束喽")

# 实例化进程对象
process = mp.Process(target = fun)

# 启动进程 进程诞生 执行fun函数
process.start()

print("诶呦我也做点事...")
sleep(3)
print("诶呦我也做完了...")

# 阻塞等待子进程退出
process.join()
print("a:",a) # 子进程一定已经结束