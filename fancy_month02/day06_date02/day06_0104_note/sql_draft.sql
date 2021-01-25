create table marathon
    (id int primary key auto_increment,
     athlete varchar(32),
     birthday date,
     registration_time datetime,
     performance time);

insert into marathon values
(1,'李卓凡','1998-10-04','2021-01-04 10:25:04','1:55:30'),
(2,'曹操','1700-10-04','2021-01-05 11:31:02','0:01:30');

insert into marathon values
(3,'张飞','1808-06-07','2021-01-04 09:28:04','2:55:30'),
(4,'关羽','1710-04-04','2021-01-05 23:31:02','3:01:30');


alter table marathon modify registration_time  datetime default now();

insert into marathon (id,athlete,birthday,performance)
values
(5,'飞哥','2005-08-08','3:05:06')


update book set price ='4.5' where book_name ='《爵迹》';
alter table book add date date after price;

insert into class (name,age,sex,score)
values
('mary',18,'f',89),
('Gry',16,'f',84),
('Hry',17,'m',79),
('Droe',14,'f',94);

insert into class (name,age,sex,score)
values
('Hos',18,'f',61),
('Gber',16,'m',74),
('joecy',17,'m',66),
('Awee',14,'f',11);

insert into class (name,age,sex,score)
values
('koer',18,'f',75),
('Wanli',16,'f',66);
 select * from sanguo where country='蜀' and attack>(select attack from sanguo where country='魏' order by attack desc limit 1);
#添加索引
 create table index_test
 (id int auto_increment,
 name varchar(30),
 primary key(id),
 index nameIndex(name));

