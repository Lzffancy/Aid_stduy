"""
编写一个函数,传入一个列表,列表中是文件名
将列表中的文件合并为1个,名字自取

列表中都是文本文件:
["../day01/1.txt","../day02/2.txt",...]
"""

def union_file(files):
    """
    将列表中的文件合并为一个
    :param files: 文件列表
    """
    fw = open("union.txt",'a')
    for file in files:
        with open(file) as fr:
            fw.write(fr.read())
            # while True:
            #     data = fr.read(1024)
            #     if not data:
            #         break
            #     fw.write(data)
    fw.close()

files = [
"../day01/1.txt",
"../day02/2.txt",
"../day03/3.txt"
]

union_file(files)



