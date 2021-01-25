## 权限管理

#### 1.用户分组权限

　组创建者(管理员) u

　组内成员 g            全部组　a 

　外部组 o

1.1 chomd a/u/g/o   +/-rwx    (文件/目录)

​     或者使用　chomd 　777 　 (文件/目录),　其各个位置的权重为ｒ4 w2 x1,以上命令表示对于ugo用户都有ｒｗx权限

#### 2.用户管理

groupadd groupdel 

useradd -m 　用户名　-g 组

userdel -r 用户

passwd ： 设置密码，设置之后才能切换新用户登录

##### 2.1增加权限

sudo vi /etc/sudoers

##### 2.2修改shell

 sudo vi etc/passwd

#### 3.软件安装apt

Linux下安装的软件包是 deb格式软件包。由于当时Linux系统中软件包存在复杂的***依赖关系***。因而，通常使用***网络安装。***

安装软件  apt   install  

卸载软件  apt   remove  --purge

#### 4.ssh服务

ssh是一种安全协议，主要用于给远程登录会话数据

##### 4.1安装启动登录

sudo apt install openssh-server

ps -e|grep ssh

sudo  service  ssh  ***start/restart/stop***

------------------------------------------------------

ssh 用户名@ip

scp　 用户名@ip:文件名或路径(服务器绝对路径)　　本地路径(默认为当前文件夹)

加上 -r 选项可以传送文件夹

#####  4.2 加入秘钥

１．生成　ssh-keygen　在用户下的.ssh文件夹内

２．将信任的计算机的id_rsa.pub文件内容追加到服务器~/.ssh/authorized_keys文件中，并修改其权限为777。

#### 5.终端启动Python服务

1.py文件第一行

＃！/usr/bin/python3

2.将py文件修改为权限777(可执行)

3.直接执行　自动调用python3

## 显示展示命令

echo 打印  

date时间　

df　磁盘用量

whoami　当前用户　(ext为磁盘)　

which命令所在位置



## 输出重定向

''>''

echo "hello world"   > out.txt，将执行结果，写到out.txt文件中，没有则创建，若**有同名文件将被删除覆盖**

">>"

ls   /usr   >> Lsoutput.txt，将ls   /usr的执行结果，***追加到***Lsoutput.txt文件已有内容后

## 软链接

ln : 一般使用  -s 选项 创建软链接，相当于快捷方式，如果跨目录创建要使用绝对路径。

## Vi

#### １．文本内容编辑器

![ms](/home/tarena/桌面/fancy02_month02/day02_fancy/day02_1228_note/ms.png)

#### ２．底行模式常用命令

wq保存退出 　　w!强制保存

#### ３．命令模式常用命令

##### 3.1行移动

０行首　　　$  行尾

gg  文件顶部   G  文件末尾

:数字   移动到 数字 对应行数

##### 3.2 命令撤销

u  撤销上次命令

CTRL + r  恢复撤销的命令

##### 3.3 删除

x    删除光标所在字符

cw        # 从光标位置删除到单词末尾
c0        # 从光标位置删除到一行的起始位置
cb       # 从光标位置删除到单词开头



##### 3.4 剪切、复制、粘贴

yy 复制一行，可以 nyy 复制多行

dd 剪切光标所在行

p 贴到下一行

##### 3.5 替换、查找

***:%s/str/replace/g***

替换所有str为replace

/str  　　查找 str　

:set nu   显示行号