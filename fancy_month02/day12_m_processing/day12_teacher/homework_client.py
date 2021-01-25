from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

def chat(msg):
    sock = socket()
    sock.connect(ADDR)
    sock.send(msg.encode())
    result = sock.recv(1024)
    sock.close()
    return result.decode()

# 创建套接字
def main():
    while True:
        msg = input("我：")
        if not msg:
            break
        result = chat(msg)
        print("小美：",result)

if __name__ == '__main__':
    main()