"""
进程间通信
"""

from multiprocessing import Process,Queue
q = Queue()

def handle():
    while 1:
        cmd=q.get()
        if cmd ==1:
            print('完成一号事件\n')
        elif cmd == 2:
            print('完成二号事件\n')

p = Process(target=handle)
p.start()
#p.join()
#print('end')

while 1:
    cmd = input("指令：\n")
    q.put(int(cmd))


