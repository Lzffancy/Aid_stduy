from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

class QueryWord:
    def __init__(self):
        self.sock = socket(type=SOCK_DGRAM)

    def close(self):
        self.sock.close()

    # 网络传输
    def recv_mean(self,word):
        self.sock.sendto(word.encode(),ADDR)
        mean,addr = self.sock.recvfrom(1024)
        return mean.decode()

    # 输入输出
    def query_word(self):
        while True:
            word = input("Word:")
            if not word:
                break
            mean = self.recv_mean(word)
            print("%s : %s"%(word,mean))


if __name__ == '__main__':
    query = QueryWord()
    query.query_word() # 查单词
    query.close()