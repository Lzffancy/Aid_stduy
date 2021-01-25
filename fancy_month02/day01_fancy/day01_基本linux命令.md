# hello markdonwn note

### Linux操作系统认知



1.操作系统是***管理计算机硬件***与***软件资源***的计算机程序

2.***内核***: Linux操作系统的核心代码，是Linux系统的心脏，提供了系统的核心功能，***用来与硬件交互***。*(cup,硬盘，内存读写等)*

3.**Linux 只是一个系统内核**

4.windows文件系统，分不同盘符*（森林结构*

   Linux的文件组织中没有盘符。将根（/）作为整个文件系统的唯一起点





### Linux常用命令(面试常考)

1.命令格式 

command   [-options]   [parameter]

### 2.常用

**touch     [文件名]**

如果文件不存在，新建文件

可以同时跟多个参数表示创建多个文件



**mv　 [文件＆目录]　[目录]**

将文件移动到目录

当前文件移动到当前目录，有重命名的作用。



**cp　[文件]　[文件２]**

在移动目录要使用　-r　参数

同时这个命令有***另存为的作用***

＃－－－－－－－－－－－－－－－－－－－

cat    [文件]

grep 　[文本]　[文件名]

find 　[目录]　-name　 [文件名]　　

wc　 [文件名]　（查看文件行数，单词数等信息

head 文件名

tail 文件名
ps 显示所有进程

＃－－－－－－－－－－－－－－－－－－－

cd 返回用户根

cd / 返回系统根

cd .. 返回上层目录

．当前目录

＃－－－－－－－－－－－－－－－－－－－

管道操作　｜

　ls /etc | wc -w

### ３．通配符*（正则）

*任意长度字符串

？一个长度字符

[ ] 匹配括号内的一个　file_[otr].txt

[ - ] 匹配范围内的一个　file_[a-z].txt

### ４．压缩解压操作

#### zip

 用于常与windows交互的情况，-r选项可以压缩目录

zip (new_file).zip  file01 file02

（压缩file01 file02到(new_file).zip

zip -d path file.zip (压缩到指定路径)

unzip  test.zip

＃－－－－－－－－－－－－－－－－－－－

#### tar

常用于Linux

tar -cjf　　  -->.tar.bz2

tar -czf 　　-->.tar.gz

解压

tar -xvf 



tar -czf   file.tar.gz   file1  file2

（将file1 和file2压缩为file.tar.gz）

tar -xvf file.tar.gz

