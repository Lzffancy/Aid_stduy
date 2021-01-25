"""
自定义进程类
"""
from multiprocessing import Process

# 创建自己的类
class MyProcess(Process):
    def __init__(self, value=1):
        self.value = value
        super().__init__() # 执行父类的init方法

    # 重写run，作为子进程执行内容
    def run(self):
        for i in range(self.value):
            print("作为进程执行")

if __name__ == '__main__':
    process = MyProcess(3)
    process.start() # 启动进程 执行run

# class Process:
#     def __init__(self,target=None):
#         self._target = target
#
#     def run(self):
#         self._target()
#
#     def start(self):
#         # 申请创建进程
#         self.run()







