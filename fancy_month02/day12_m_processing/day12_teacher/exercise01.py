"""
编写一个程序，将一个大文件拆分为2个小文件
上半部分拆为一个，下半部分一个，按照字节大小划分

要求： 拆分过程需要同时执行，分别用两个子进程完成
      查分完成后，打印提示 "拆分完毕"

提示： os.path.getsize()
      file.seek()

难点： 不允许一次读取一半
"""

from multiprocessing import Process
import os

filename = "./glnz.jfif"
size = os.path.getsize(filename)

# 如果父进程打开文件，子进程直接使用fr，那么
# 父子进程用的是同一个文件偏移量会相互影响
# fr = open(filename,'rb')

# 拆出上半部分
def top():
    fr = open(filename,'rb')
    fw = open("top.jpg",'wb')
    n = size // 2 # 要复制n个字节
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()


# 拆出下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open("bot.jpg", 'wb')
    fr.seek(size//2,0) # 文件偏移量到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

# 启动函数 创建进程
def main():
    jobs = []
    # 创建2个子进程
    for th in [top,bot]:
        p = Process(target=th)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs] # 等待拆分结束
    print("拆分完毕")

if __name__ == '__main__':
    main()








