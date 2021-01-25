"""
如何创建一个多进程？
"""
import time


def fun01():
    print('我是ｆｕｎｃ０１被执行了！！！')

def fun02():
    print('我是ｆｕｎｃ０2被执行了！！！')

def fun03():
    print('我是ｆｕｎｃ０3被执行了！！！')

from multiprocessing import *

#使用Process类实例化来绑定　需要多进程执行的函数
# 但是这里有多个函数需要建立多进程
#　采用ｆｏｒ循环

for th in [fun01,fun02,fun03]:
    p = Process(target=th)
    # 父进程下３个子进程，同等级交给ｃｐｕ
    # 并且拥有父进程中的所有环境
    p.start()
    # 设置父亲进程等待子进程,避免产生孤儿进程
    # 当python执行到p.start()，p.join()　也会自动处理掉僵尸进程
    p.join()


#当进程需要传递参数,在绑定的时候设置arges,或者kwarges
def fun04(a):
    print(a,'我是ｆｕｎｃ０4被执行了！！！')


p2 = Process(target=fun04,kwargs={'a':"我哦我哦我是参数"},daemon=1)
p2.start()

# 父亲进程先结束，p2不会执行，所以ｓｌｅｅｐ执行
#time.sleep(5)