--表的创建
create table class (
name varchar(30),
age tinyint,
sex enum('m','f','o'),
score float
);


create table class (
id int primary key auto_increment,
name varchar(30) not null,
age tinyint unsigned,
sex enum('m','f','o'),
score float default 0
);


create table hobby (
id int primary key auto_increment,
name char(30) not null,
hobby set("sing","dance","draw"),
level char  comment "评级",
price decimal(7,2),
remark text  comment "备注信息"
);

--数据插入
insert into class values
(1,"Lily",18,'f',89),
(2,"Lucy",18,'f',76),
(3,"Tom",17,'m',83);

insert into class
(name,age,sex,score)
values
("Levi",18,'m',86),
("Sunny",17,'m',91),
("Eva",17,'f',71);

insert into hobby
(name,hobby,level,price,remark)
values
("Joy","sing,dance","A",56800,"骨骼惊奇"),
("Abby","sing","B",14800.888,"天籁之音"),
("Barom","draw","B",26800.00,"当代达芬奇");

insert into hobby
(name,hobby,level,price)
values
("Jame","dance","C",8800),
("Emma","draw,sing","B",44800),
("Chen","sing","C",16800);


练习01：
创建一个数据库  books

create database books charset=utf8;
use books;

创建一个数据表  book  类型和约束自己设计
字段 ： id  书名   作者   出版社  价格   备注
create table book (
id int primary key auto_increment,
bname varchar(50) not null,
author varchar(30),
press varchar(50),
price float,
comment text
);


向其中插入数据若干  >= 5条
参考 ： 老舍  沈从文  鲁迅  冰心  ....
出版社 ： 中国文学  人民教育   机械工业
价格 ：  30-120

insert into book
(bname,author,press,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么？"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","中国文学出版社",44,"你心中的围城是什么");

insert into book
(bname,author,press,price)
values
("林家铺子","茅盾","机械工业出版社",51),
("巨人传","忘了","人民教育出版社",47);

查询练习02  book表
​
1. 查找30多元的图书
select * from book
where price >= 30 and price < 40;

２．查找人民教育出版社出版的图书　
select * from book
where press = "人民教育出版社";

３．查找老舍写的，中国文学出版社出版的图书　
select * from book
where author="老舍" and press="中国文学出版社";

４．查找备注不为空的图书
select * from book where comment is not null;

５．查找价格超过60元的图书，只看书名和价格
select bname,price from book where price>60;

６．查找鲁迅写的或者茅盾写的图书
select * from book
where author ="鲁迅" or author="茅盾";

select * from book
where author in ("鲁迅","茅盾");
