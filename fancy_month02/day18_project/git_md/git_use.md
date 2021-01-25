# GIT & GItHub

GIT是一个开源的分布式版本控制系统
GItHub 是使用该控制系统的开发者社区



## 1.GIT 原理

![git](/home/tarena/桌面/fancy_month02/day18_project/git_md/img/git.jpeg)

基本概念

* 工作区(worksapce)：项目所在操作目录，实际操作项目的区域
* 暂存区(index): 用于记录工作区的工作（修改）内容
* 仓库区(repository): 用于备份工作区的内容
* 远程仓库(remote): 远程主机上的GIT仓库

> 注意： git总是希望worksapce的内容与repository保持一致***(及时commit）***
> 且只有repository的内容才能和其他remote仓库交互。

## 2.GIT 配置

### 2.1 开始

```shell
#linux 下安装git
sudo apt  install  git

#初始　配置
git version        #查看版本
sudo git config --global user.name Tedu
git config --global user.email lvze@tedu.cn


git config --list  #查看配置信息

```

### 2.2 仓库

```shell
#将当前目录作为git操作目录,并生成git本地仓库
#此目录默认工作于master分支
git  init 

git  status  #查看仓库状态
```

### 2.3 暂存区

```shell
#工作内容记录到暂存区(跟踪)
git add [...]
#取消文件暂存记录
git rm --cached [...]


#暂存区　文件同步到 本地仓库
git commit [file] -m ['message']
说明: -m表示添加一些同步信息，不加file表示同步所有index区的文件,message必须填写


git log #查看提交日志

#将暂存区　或者某个commit点文件恢复到工作区
git checkout [commit] -- [file]
e.g. 将a.jpg文件恢复,不写commit表示'恢复最新'保存的文件内容
git checkout  --  a.jpg

# 移动或者删除文件
git  mv  [file] [path]
git  rm  [files]
注意: 这两个操作会修改工作区内容，'同时将操作记录提交到暂存区。

```

 项目根目录添加**.gitignore**文件的方式，规定相应的忽略规则
此文件中描述的文件将不会添加到index区

```shell
.gitignore忽略规则简单说明

file            表示忽略file文件
*.a             表示忽略所有 .a 结尾的文件
!lib.a          表示但lib.a除外
build/          表示忽略 build/目录下的所有文件，过滤整个build文件夹；
```

## 3.版本控制

```shell
# 退回到上一个commit节点
git reset --hard HEAD^
#退回到指定的commit_id节点
git reset --hard [commit_id]
#查看所有操作记录
git reflog
```

为里程碑版本***添加标签***

```shell
git  tag  [tag_name] [commit_id] -m  [message]
git tag v1.0 -m '版本1'

git tag  查看标签列表
git show [tag_name]  查看标签详细信息

git tag -d  [tag]
```

## 4.分支管理

分支即每个人在原有代码（分支）的基础上建立自己的工作环境，完成单独开发，之后再向主分支统一合并工作内容。

***子分支会　拥有父分支的代码***

```shell
git branch　#查看现有分支
说明: 前面带 * 的分支表示当前工作分支

# 创建分支
git branch [branch_name]
说明: 基于a分支创建b分支，此时b分支会拥有a分支全部内容。在创建b分支时最好保持a分支工作区"干净"状态。

# 切换工作分支
git checkout [branch]
# 创建并切换分支
git checkout -b [branch]

#　合并分支
git merge [branch]
# 删除分支　
git branch -d [branch] 
git branch -D [branch]  删除没有被合并的分支
```

### 4.1分支冲突问题

***冲突情形1***
原来的分支增加了新文件或者原有文件发生了变化
此时只要先摁 **ctrl-o** 写入，然后回车，再摁**ctrl-x** 离开就可以了。

***冲突情形2***
子分支和父分支修改了相同的文件
这种冲突不太好解决需要自己进入文件进行修改后，再执行add ，commit操作提交

总结

* 尽量在项目中***降低耦合度***，不同的分支只编写自己的模块。
* 如果必须修改原来父级分支的文件内容，那么做好分工，***不要让******多个分支都修改同一个文件***。

# GitHub

## 1.获取一个项目

```
#在本地使用git clone方法即可获取
git clone https://github.com/xxxxxxxxx
```

注意:

1. 获取到本地的项目会自动和GitHub远程仓库建立连接。且获取的项目本身也是个git项目。
2. GitHub提供两种地址链接方式，http方式和SSH方式。通常访问自己的项目可以使用SSH方式，clone别人的项目使用http方式。  

## 2.创建自己的项目

### 添加SSH密钥

```shell
# 先建立秘钥信任
1. 将自己要连接github的计算机的ssh公钥内容复制
2. github上选择头像下拉菜单，settings-》SSH and GPG keys-》new SSH key
```

### 在本地使用ssh连接仓库

```shell
# 后续操作每次上传内容都需要输入密码，比较麻烦，一般用于临时计算机的连接使用
git remote  add origin git@github.com:/tarena/aid.git

注意：
如果连接远程时 git remote add origin 后用https地址，那么以后每次上传内容都需要输入用户名密码
```

remote

```shell
# 查看连接的远程仓库名称 ,列出已经存在的远程分支
git remote
# 断开远程仓库连接(删除origin)
git remote rm [origin]

git push -u origin  master
将master分支推送给origin主机远程仓库，"第一次"推送分支使用-u表示与远程对应分支	建立自动关联

# 有修改项推送给远程仓库
git push

# 强行推送本地版本
git push --force origin

# 从远程获取代码
git pull
```





