"""
event 线程同步互斥方法
"""
from threading import Thread, Event

msg = None  # 通信变量
e = Event()  # 事件对象


def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set()  # 通知主线程可以判断


t = Thread(target=杨子荣)
t.start()

print("说对口令才是自己人")
e.wait()  # 阻塞等待通知
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神你是对的人")
else:
    print("打死他.... 无情啊 哥哥....")
