"""
establish multiprocessing with args kwargs
"""
import multiprocessing as mp
from time import *
import os

def worker(sec,name):
   for i in range(3):
       sleep(sec)
       print("im %s" % name)
       print('im working..')
       print(os.getpid())


# creat process object
process01 = mp.Process(target=worker,args=(2,'fancy'))
process02 = mp.Process(target=worker,
                       kwargs={'sec':2,'name':'jojo'},
                       daemon=True)
# process start💩
process02.start()
sleep(10)
process01.start()



# -----------------
