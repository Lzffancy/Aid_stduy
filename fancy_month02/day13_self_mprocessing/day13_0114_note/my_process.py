"""
自定义进程
"""
from multiprocessing import *


class MyProcess(Process):
    def __init__(self, value=1):
        self.value = value
        # super　同时继承父类的实例变量
        super().__init__()

    def run(self) -> None:
        for i in range(self.value):
            print(i, '自定义进程执行run内重写功能')


if __name__ == '__main__':
    p1 = MyProcess(100)
    p1.start()
