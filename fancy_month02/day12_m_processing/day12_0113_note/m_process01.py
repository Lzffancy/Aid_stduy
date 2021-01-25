"""
establish multiprocessing
"""
a = 1
import multiprocessing as mp
from time import *


# func
def func():
    global a
    print('process01 begin...')
    sleep(5)
    a = 111111111111111111111111
    print('process01 end!!')



# creat process object
process01 = mp.Process(target=func)

# process start💩
process01.start()

# -----------------

print('other thing begin..')
sleep(2)
print('other thing end !!')
# wait 子进程
process01.join()
print("----------------------------")
print('a:', a)
