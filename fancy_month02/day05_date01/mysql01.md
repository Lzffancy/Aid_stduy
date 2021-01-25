# 数据库基本操作

## 1. Ｗhat is MySQL?

结构化查询语言Structured Query Language

* 定义：数据库是在数据库管理系统管理和控制下，在一定介质上的数据集合。

* 优缺点

优点 ： 数据组织结构化降低了冗余度,提高了增删改查的效率,容易扩展,方便程序调用处理,早期是开源数据库

缺点 ： 需要使用sql 或者其他特定的语句，相对比较专业

*　类型

关系型： 采用关系模型（***二维表***,如行｜列）来组织数据结构的数据库 ，如<u>***Oracle***</u> 、SQL_Server、 MySQL

非关系型： 不采用关系模型组织数据结构的数据库，如：MongoDB、Redis

## 2. 启动

sudo  service  mysql    start/stop/restart/status  #启动　# 状态

mysql  -h  ip   -u    id   -p     #连接　　id使用root具有最高权限

### 2.1 MySQL数据库结构

数据元素 --> 记录 -->数据表 --> 数据库

* 数据表（table） ： 存放数据的表格 (在库中可放多个表)
* 字段（column）： 每个***列***，用来表示该列数据的含义（列标题，数据抽象）
* 记录（row）： 每个***行***，表示一组完整的数据（实例）

注意：

* 每条命令以 ; 结尾
* SQL命令（除了数据库名和表名）关键字和字符串可以不区分字母大小写

## 3. 创建库

create database 库名 [character set utf8];

show databases;

use 库名;

select database();    #当前库

drop database 库名;

## 4. 表设计

基本思考过程

1. 确定存储内容

2. 明确字段构成

3. 确定字段数据类

### 4.1数字

   　tinyint 　　　1字节

   　smallint　　２字节 

　　mediumint 　3字节

   　int　　　　　４字节 

   　bigint　　　　８字节

   　 float 　　　　４字节

   　double　　　８字节

   　decimal　　

4. > 1. decimal,准确性较高，比如money，声明语法是decimal(M,D)。M是数字的最大数字位数，D是小数点右侧数字的位数，带符号
   > 2. bit类型10 真假
   > 3. tinyint(4)最多显示４位，但实际储存还是一个字节

   

![shuzi](/home/tarena/桌面/fancy_month02/day05_fancy/day05_1231_note/shuzi.png)

### 4.2 字符

char 　定长，即指定存储字节数后，无论实际存储了多少字节数据，最终都占指定的字节大小。默认1字节数据。(50字节以下char(10))

varchar　不定长，节省空间，实际占用空间根据实际存储数据大小而定。***必须要指定存储大小*** varchar(50)

text 大量文本

blob 二进制数据(图片，音频)

enum 单选，enum('A','B','C')

set 多选，set('A','B','C')



### 4.3 时间

date 　3字节　　年月日

datetime   8字节 　　　年月日　时分秒  

timestamp 4字节　　　年月日　时分秒（与datetime表示形式相同但储存数据格式不同）

time 3字节

year 

```sql
date ："YYYY-MM-DD"
time ："HH:MM:SS"
datetime ："YYYY-MM-DD HH:MM:SS"
timestamp ："YYYY-MM-DD HH:MM:SS"
```

使用当前时间为默认值
default now()            #datetime

## 5. 创建表

>create table 表名
>(字段名 数据类型 约束,
>字段名 数据类型 约束,
>字段名 数据类型 约束);

### 5.1 约束

unsigned  #必须跟在数据类型后面；

not null

default

primary key   #主键的值不能重复,且不能为空　auto_increment #自增

commet

```sql
e.g.  创建班级表
create table class (id int primary key auto_increment,
                    name varchar(32) not null ,
                    age tinyint unsigned not null,
                    sex enum('w','m'),
                    score float default 0.0);
```



### 5.2 表操作

show tables;

show  create  table  表名；　　＃创建信息

desc  表名;   #(describe)表结构 

drop  table  表名;

show full columns from 表名；

## 6.表数据操作

#### insert into [table]

```sql
e.g. 
insert into class values 
(2,'Baron',10,'m',91),
(3,'Jame',9,'m',90);

insert into class 
(name,age,sex,score) values 
('Lucy',17,'w',81);
```

#### select  [cols] from

```sql
select * from 表名 [where 条件];
select 字段1,字段2 from 表名 [where 条件];
```

#### update   [tab]   set   [col1..]

```sql
update 表名 set 字段1=值1,字段2=值2,... where 条件;
注意:update语句后如果不加where条件,所有记录全部更新
```

#### delete from [tab]

```sql
delete from 表名 where 条件;
注意:delete语句后如果不加where条件,所有记录全部清空
```

#### where  可执行的运算

* 　　算数运算符

  +-*/%

* 比较运算符

  =   !=  >   <  <=  >=    between     not between  

* 逻辑运算符

  not    and   or         is null

#### alter table [tab]  [add\drop\modify\change]  [clo..]

修改数据类型(modify)

修改字段名(change)

```sql
* 添加字段(add)
    alter table 表名 add 字段名 数据类型;
    alter table 表名 add 字段名 数据类型 first;
    alter table 表名 add 字段名 数据类型 after 字段名;
* 删除字段(drop)
    alter table 表名 drop 字段名;
* 修改数据类型(modify)
    alter table 表名 modify 字段名 新数据类型;
* 修改字段名(change)
    alter table 表名 change 旧字段名 新字段名 新数据类型;
```

























