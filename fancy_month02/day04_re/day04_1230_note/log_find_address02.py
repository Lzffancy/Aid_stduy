'''
to find Hardware address
'''

import re
log_path = '/home/tarena/桌面/fancy_month02/day03_fancy/data_teacherdoc/info/inet.log'


def find_Hd_address(name='', path=''):
    pass


def info(path):
    with open(path) as f:
        while 1:
         data = ''
         for line in f:
            if line == "\n":  # 整行只有换行符
                break
            data += line

         if data:
            print(data)
            yield data
         else:
            return None


def hd_address(prot_name, path):
    """

    :param prot_name: 端口名
    :param path: log文件位置
    :return: 硬件地址
    """
    for data in info(path):
        head = re.match('\S+', data).group()
        if prot_name == head:
            result = re.search("([0-9a-f]{4}\.){2}[0-9a-f]{4}", data)
            return result.group()


if __name__ == '__main__':
    # while 1:
    name = input("端口名：")
    print('硬件地址：', hd_address(name, log_path))
