'''
对话小程序，客户端可以发送问题给服务端
服务端接收到问题 将对应答案给客户端，客户端打印出来
要求可以同时多个客户端提问，如果问题没有指定答案
则回答 “人家还小，不知道。”

接收问题 返回答案

通过字典查答案
server
'''
from socket import *
anwser_dict={         '岁': "我三岁了!",
                      '是谁': '我是人工智障',
                      '?': '你凭什么给我发问号?',
                      "好": "我不好",
                      '哈': "闭嘴!!不许笑",
                      "名": '我叫AI,Fancy',
                      '喜': '妈妈不让',
                      '大':"我18,嘿嘿"}

class Dialog_server():
    # 服务器初始化配置,socket 创建
    def __init__(self):
        S_ADDR = ('0.0.0.0', 65534)
        self.socket_s = socket(AF_INET, SOCK_STREAM)
        self.socket_s.bind(S_ADDR)
        self.socket_s.listen(20)

    def find_how_to_anwser(self, recive_data):
        # recive_data = '你几岁啦'
        # 单个关键字触发,    不可以多条件,指向同一回答  比如"年龄",'岁数"  :"男的女的",'性别'
        key_anwser = anwser_dict
        for item in key_anwser:
            for str_item in recive_data:
                if item in str_item:
                    return key_anwser[item]
        else:
            return "人家还小，不知道。"

    def recive_req(self):
        """
        接收客户问题
        :return: 问题答案
        """
        # 接收客户端 connect
        print('waiting connet...')
        c_connfd, c_addr = self.socket_s.accept()
        print('connet from ', c_addr)
        # 接收客户端消息
        recive_data = c_connfd.recv(128)

        # 准备答案
        anwser = self.find_how_to_anwser(recive_data.decode())
        # 回答案给客户端
        c_connfd.send(anwser.encode())
        # 断开与该客户连接
        c_connfd.close()


if __name__ == '__main__':
    dialog_s = Dialog_server()

    while 1:
        # 会话一次断开一次
        dialog_s.recive_req()
