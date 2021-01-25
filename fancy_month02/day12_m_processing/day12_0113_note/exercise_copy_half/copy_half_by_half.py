"""
提示： os.path.getsize()
      file.seek()
难点： 不允许一次读取一半
"""

from multiprocessing import *
import os

filename = './1.txt'
#getsize 读字节数
f_size = os.path.getsize(filename)

# 如果父进程打开文件，子进程直接使用fr，那么
# 父子进程用的是同一个文件偏移量会相互影响
# fr = open(filename,'rb')


def split_top():
     fr = open(filename,'rb')
     fw = open('top.txt','wb')

     n = f_size//2  #复制前ｎ个字节
     while n >= 1024:
         fw.write(fr.read(1024))
         n -= 1024
     else:
         fw.write(fr.read(n))
     fr.close()
     fw.close()


def split_bot():
    fr = open(filename, 'rb')
    fw = open('bot.txt', 'wb')
    fr.seek(f_size//2,0) #从中间开始读

    while 1:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()



def main():
    # 开启所有进程
    jobs =[]
    for th in [split_top,split_bot()]:
        p = Process(target=th)
        p.start()
    # 父进程等待所有子进程
    [i.join() for i in jobs]
    print('split ok')

if __name__ == '__main__':
    main()