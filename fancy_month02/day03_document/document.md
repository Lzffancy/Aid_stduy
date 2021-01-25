## What is data?

* 数据 ： 能够输入到计算机中并被识别处理的信息集合

* 数据处理：数据处理的基本目的是从大量的、可能是杂乱无章的、难以理解的数据中抽取并推导出对于某些特定的人们来说是有价值、有意义的数据。

* ```
  字节串（bytes)
  (表达二进制的一种类型)
  1.所有的　字符串　都可以对应上相应的字节串
  2.但字节串不一定对应字符串　，还可以对应其他
  3.str.encode()
    bytes.decode()
  ```

## what is file?

* 文件：保存在持久化存储设备(硬盘、U盘、光盘..)上的一段数据

* 文件分类：

  　文本文件：打开后会自动解码为字符，如txt文件，word文件，py程序文件。

    　二进制文件：内部编码为二进制码，如压缩包，音频，视频，图片等。

What is Function?

参数、过程、返回值

### 1. 文件读写

* file_object = open(file_name, access_mode='r', buffering=-1，encoding=None)

 ### 1.1 access_mode

r 只读（已有文件）

w覆盖写，无则创建（会先清空　　　 

a追加写 ，无则创建

＋　添加读｜写　　

b　以二进制

 ### 1.2 读取 .read(size)

 1.读到文件结尾如果继续进行读操作***会返回空字串***。

 2.readlines([sizeint])　读取每一行输出为列表

 3.文件对象本身也是一个可迭代对象，在for循环中可以迭代文件的每一行。（输出为str

```
# f = open("1.txt", 'r') #可迭代对象
# while 1:
#  content = f.read(2) #2的n次方倍　　此方式在读取大文件有优势
#  print(content,end="")
#  if content==None:
#      break
```



### 1.3 写.write(size)

1.writerlines(str_list)　接受列表，写入文件

### 1.4 关闭 .close()

with open() as f

### ２. 读写刷新缓存

```
刷新缓冲
f.flush()　手动刷新
buffering=1　换行刷新
buffering=10　按照bytes刷新,写入二进制
```

flush()　open(buffering=)

在对文件读写时都是先将文件内容加载到缓冲区（内存），再进行读写到硬盘．

* 作用

1. 减少和磁盘的交互次数，保护磁盘。
2. 提高了对文件的读写效率。

### ３. 文件偏移量（指针

.tell()  返回值：文件偏移量

.seek(offset,whence)  　

　　offset指针移动数

　　whence　０开始位置　１当前位置　２末尾位置

（必须以二进制方式打开文件时，基准位置才能是1或者2）ｗ+ 偏移量会在末尾

## What is OS?

os.path.getsize(file)  #文件大小

os.listdir(dir)　　　　#文件目录

os.path.exists(file)　#文件存在

os.remove(file)　　　#删除文件

