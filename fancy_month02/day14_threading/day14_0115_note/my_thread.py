'''
自定义线程
'''
from threading import Thread
from time import sleep


class Mythread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__()

    def run(self):
        for i in range(3):
            sleep(1)
            print('播放：',self.song)

t = Mythread('２００２年的第一场雪')
t.start()

