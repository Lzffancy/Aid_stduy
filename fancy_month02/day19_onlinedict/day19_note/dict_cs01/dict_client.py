"""
dict 客户端
"""
from socket import *
import os
# 服务端地址
ADDR = ("127.0.0.1",8800)

# 发起请求 逻辑处理
class DictHandle:
    def __init__(self):
        self.sock = self.__create_socket()

    def __create_socket(self):
        sock = socket()
        sock.connect(ADDR)
        return sock

    # 完成注册
    def do_register(self):
        while True:
            name = input("Name:")
            passwd = input("Passwd:")

            # 验证
            if " " in name  or " " in passwd:
                print("用户名密码不能有空格")
                continue
            # 发送请求
            msg = "R %s %s"%(name,passwd)
            self.sock.send(msg.encode())
            result = self.sock.recv(128).decode()
            # 根据结果讨论
            if result == 'OK':
                print("注册成功")
                return 1
            else:
                print("注册失败")
                return 0
#
    def do_login(self):
        while True:
            name = input("Name:")
            passwd = input("Passwd:")
            # 发送请求
            msg = "L %s %s" % (name, passwd)
            self.sock.send(msg.encode())
            result = self.sock.recv(128).decode()
            # 根据结果讨论
            if result == 'OK':
                print("登录成功")
                return 1
            else:
                print("登录失败")
                return 0
    def do_exit(self):
         self.sock.send(b"E")

    def do_query(self):
        pass

# 视图交互

class DictView:
    def __init__(self):
        self.handle = DictHandle()

    # 二级界面
    def __menu_2(self):
        while True:
            print("""
        =============== Query ==============
         1. 查单词     2. 历史记录    3. 注销
        ====================================
            """)
            item = input("请输入选项:")
            if item == "1":
                pass
            elif item == "2":
                pass
            elif item == "3":
                break
            else:
                print("请输入正确选项!")

    # 一级界面
    def __menu_1(self):
        while True:
            print("""
            =========== Welcome =============
             1. 登录     2. 注册    3. 退出
            =================================
            """)
            item = input("请输入选项:")
            if item == "1":
                 if self.handle.do_login():
                     self.__menu_2()
                 else:
                     self.__menu_1()
            elif item == "2":
                if self.handle.do_register():
                   self.__menu_2()
                else:
                   self.__menu_1()
            elif item == "3":
                return
            else:
                print("请输入正确选项!")

    def main(self):
        self.__menu_1()

        return print('bye~')

if __name__ == '__main__':
    dict = DictView()
    dict.main() # 入口方法