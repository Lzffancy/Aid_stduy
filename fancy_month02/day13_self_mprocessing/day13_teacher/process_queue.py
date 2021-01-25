"""
消息队列实现进程间通信
"""
from multiprocessing import Process,Queue

# 创建消息队列
q = Queue(10)

# 事件处理函数
def handle():
    while True:
        cmd = q.get() # 取出指令
        if cmd == "1":
            print("\n完成1号事情")
        elif cmd == "2":
            print("\n完成2号事情")

p = Process(target = handle)
p.start()

while True:
    cmd = input("指令：")
    q.put(cmd) # 输入指令放入消息队列




