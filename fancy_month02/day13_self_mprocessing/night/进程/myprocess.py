"""
自定义进程类
"""

from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, value):
        self.value = value
        # 调用父类init保留父类属性
        super().__init__()

    def fun1(self):
        print("列表中一共有%s个元素" % len(self.value))

    def fun2(self):
        print("列表中的元素为：")
        for v in self.value:
            print(v, end=" ")

    # 进程做的事情
    def run(self):
        self.fun1()
        self.fun2()


p = MyProcess([1, 2, 3, 4, 5])
p.start()  # 运行run'作为一个进程
p.join()
