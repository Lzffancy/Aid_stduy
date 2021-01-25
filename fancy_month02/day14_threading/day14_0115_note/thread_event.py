"""
设置event  set  添加等待阻塞
"""

from threading import Event, Thread

msg = None
ev = Event()


def process_send():
    print('是我')
    global msg
    msg = "小鸡炖蘑菇"
    print(msg)
    ev.set()


t = Thread(target=process_send)
t.start()

print("黑话！天王盖地虎！")
ev.wait()
if msg == "小鸡炖蘑菇":
    print('嗨呀！好兄弟')
else:
    print("你不对！！系内！！")
