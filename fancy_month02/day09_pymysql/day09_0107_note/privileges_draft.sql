grant all privileges on *.* to 'fancy'@'%' identified by '123456' with grant option;


create table words
(
id int primary key auto_increment,
word varchar(15),
mean varchar(255)
)




create table user
(
id int primary key auto_increment,
user char(30),
password char(64)
)