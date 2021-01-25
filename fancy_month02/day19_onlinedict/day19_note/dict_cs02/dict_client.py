"""
dict 客户端
 8bit(位)=1Byte(字节)
 1024Byte(字节)=1KB
 1024KB=1MB 1024MB=1GB 1024GB=1TB
"""
from socket import *
import sys

# 服务端地址
ADDR = ("127.0.0.1",8883)

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
            else:
                print("注册失败")
            return

    # 登录请求
    def do_login(self):
        name = input("Name:")
        passwd = input("Passwd:")
        # 发送请求
        msg = "L %s %s" % (name, passwd)
        self.sock.send(msg.encode())
        result = self.sock.recv(128).decode()
        # 根据结果讨论
        if result == 'OK':
            print("登录成功")
            return name
        else:
            print("登录失败")

    def do_exit(self):
        self.sock.send(b"E")

    def do_query(self,name):
        while True:
            word = input("Word:")
            if word == "##":
                break
            msg = "Q %s %s"%(name,word)
            self.sock.send(msg.encode())
            # 接收结果，直接打印
            mean = self.sock.recv(1024 * 10).decode()
            print("%s : %s"%(word,mean))


    def do_hist(self,name):
        msg = "H %s" % name
        self.sock.send(msg.encode())
        while True:
           hist = self.sock.recv(1024).decode()
           if hist == '##':
              break
           print("%s"%hist)
        print("over")



# 视图交互
class DictView:
    def __init__(self):
        self.handle = DictHandle()

    # 二级界面
    def __menu_2(self,name):
        while True:
            print("""
        =============== Query ===============
         1. 查单词     2. 历史记录    3. 注销
        =========================User:%s=====
            """%name)
            item = input("请输入选项:")
            if item == "1":
                self.handle.do_query(name)
            elif item == "2":
                self.handle.do_hist(name)
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
                name = self.handle.do_login()
                if name:
                    self.__menu_2(name)
            elif item == "2":
                self.handle.do_register()
            elif item == "3":
                self.handle.do_exit()
                sys.exit("谢谢使用")
            else:
                print("请输入正确选项!")

    def main(self):
        self.__menu_1()

if __name__ == '__main__':
    dict = DictView()
    dict.main() # 入口方法