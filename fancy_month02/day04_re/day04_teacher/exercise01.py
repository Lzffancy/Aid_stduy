"""
基于 inet.log完成
编写程序，通过输入一个端口名称（每段首个单词）
打印出这个端口描述信息中的address is 的值

提示： 段落之间有空行
      端口名称是每段第一个单词

思路： 根据输入的端口名称找到段落
      在段落中匹配目标
"""
import re


# 生成器函数  每次提供一段内容
def info():
    file = open("inet.log")
    while True:
        data = ""
        for line in file:
            if line == '\n':
                break
            data += line

        # 如果一段内容为空 则文件结束
        if data:
            yield data  # 提供一段内容
        else:
            file.close()
            return


# 从段落中匹配内容
def address(port):
    """
    :param port: 端口名称
    :return: 匹配到的 address 值
    """
    # 判断data是不是我要的段落
    for data in info():
        # 提取首个单词
        head = re.match("\S+", data).group()
        if port == head:
            # 开始匹配address
            result = re.search("([0-9a-f]{4}\.){2}[0-9a-f]{4}", data)
            return result.group()


if __name__ == '__main__':
    port = input("输入端口名称：")
    print("获取值:",address(port))
