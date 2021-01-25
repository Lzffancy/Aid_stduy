create table fancy_information (name varchar(10),age tinyint());


create table class (ID int primary key auto_increment,
                    name varchar(10) not null,
                    age tinyint unsigned,
                    sex enum('m','f','o'),
                    core float default 0);

create table hobby (id int primary key auto_increment,
                    name char(10) not null,
                    hobby set('sing','dance','darw','python'),
                    level char comment'评级越高越值钱',
                    price decimal(7,2),
                    remark text comment'备注');

insert into class values
(1,'fancy',18,'m',100),
(2,'tom',25,'f',95),
(3.,'lucy',25,'f',85);


insert into class
(name,age,core)
values
('jot',19,81),
('alxe',25,77);

#!!!!!!!!!!!!!!!!!!!!!!!
insert into hobby
(name,hobby,level,price,remark)
values
('fancy','python,dance','S','999','天下第一'),
('Emma','sing,dance,darw','A','8208','全能型');



create table book (id int primary key auto_increment,
                    book_name varchar(50) not null,
                    author varchar(20) default'佚名',
                    publisher varchar(50)default'未知',
                    price decimal(5,2),
                    remark text comment'备注');


insert into book
(book_name,author,publisher,price,remark)
values
('《爵迹》','郭敬明','人民科幻出版社',30.1,'盗版东西没人看'),
('《走在人生边上》','杨绛','人民文学出版社',80.2,'钱钟书回忆录'),
('《围城》','钱钟书','机械工业出版社',55.3,'文学讽刺'),
('《活着》','余秀华','中国文学出版社',30.2,'余秀华事迹改编'),
('《天龙八部》','金庸','劳动局出版社',99.8,'武侠玄幻'),
('《骆驼祥子》','老舍','希望科学出版社',35.1,'封建文学讽刺'),
('《华盖集》','周树人','天下第一出版社',40.2,'鲁迅散文整理');