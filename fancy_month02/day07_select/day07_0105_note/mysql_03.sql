alter table person add
constraint dept_fk     #以foreign key的值建立约束，约束名为　dept_fk 　（constraint)
foreign key(dept_id)
references dept(id);




insert into person values
(7,'fancy',19,30000,9);

insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
(6,'总裁办公室');


insert into person values
(1,"Lily",29,20000,2),
(2,"Tom",27,16000,1),
(3,"Joy",30,28000,1),
(4,"Emma",24,8000,4),
(5,"Abby",28,17000,3),
(6,"Jame",32,22000,3);


alter table person add
constraint dept_fkk
foreign key(dept_id)   #语法
references dept(id)


alter table person add

foreign key(dept_id)
references dept(id)

on delete cascade on update cascade;
#设置级联更新

#------------------------------------------------------------
create table athlete (
  id int primary key AUTO_INCREMENT,
  name varchar(30),
  age tinyint NOT NULL,
  country varchar(30) NOT NULL
);

create table item (
  id int primary key AUTO_INCREMENT,
  rname varchar(30) NOT NULL
);

CREATE TABLE athlete_item (
   id int primary key auto_increment,
   aid int NOT NULL,
   tid int NOT NULL,
   FOREIGN KEY (aid) REFERENCES athlete (id),
   FOREIGN KEY (tid) REFERENCES item (id)
);








#-----------------------------------------------------------------
create table users (
   id int primary key auto_increment,
   name varchar(20) not null,
   password varchar(20) not null,
   tel int unsigned
);

create table friend_circles(
   id int primary key auto_increment,
   str text not null,
   pic varchar(30),
   pos varchar(128),
   time datetime default now(),

   users_id int,
   foreign key(users_id) references users(id)
);

create table action_realation(
   id int primary key auto_increment,
   comt varchar(30),
   likes bit,

   u_id int,
   fc_id int,
   foreign key(u_id)  references users(id),
   foreign key(fc_id)  references friend_circles(id)

);

--------------------------------------





select person.name ,dept.dname,person.salary
from person inner join dept on person.dept_id = dept.id


#-homework-------------------------------------------

1.
select tname,count(cname)
from teacher left join course
on teacher.tid = course.teacher_id
group by tname;


2.
select sname,gender,caption
from student left join class
on student.class_id = class.cid;


3.
#如果在字段中要出现cid　那么在分组中也要进行cid分组
select cname,max(number),min(number)
from course left join score
on score.course_id = course.cid
group by course.cname;


4.
select student.sid,student.sname,avg(number)
from student left join score
on student.sid = score.student_id
group by student.sid,student.sname
having avg(number)>85;

5.
select student.sid,student.sname
from student left join score on student.sid = score.student_id
where score.course_id = 2 and score.number >80
group by student.sid,student.sname





6.
select course.cname,count(score.student_id)
from course left join score
on course.cid = score.course_id
group by  course.cname;
#btree 索引和ｈａｓｈ索引

