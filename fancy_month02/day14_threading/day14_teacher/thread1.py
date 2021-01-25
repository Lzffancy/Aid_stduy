"""
线程创建示例 1
"""
import threading
from time import sleep
import os

a = 1

#  线程函数
def music():
    global a
    print("a =",a)
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:黄河大合唱")

# 实例化线程对象
thread = threading.Thread(target=music)
# 启动线程 线程存在
thread.start()

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放:葫芦娃")

# 阻塞等待分支线程结束
thread.join()
print("a:",a)