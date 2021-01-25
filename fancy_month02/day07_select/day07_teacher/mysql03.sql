-- 外键部分
insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
6,'总裁办公室');


insert into person values
(1,"Lily",29,20000,2),
(2,"Tom",27,16000,1),
(3,"Joy",30,28000,1),
(4,"Emma",24,8000,4),
(5,"Abby",28,17000,3),
(6,"Jame",32,22000,3);


练习：
完成朋友圈数据表的设计和实现
要求 通过E-R模型图进行分析，然后完成表创建

用户表
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(60),
tel char(16)
);


朋友圈
create table pyq(
id int primary key auto_increment,
image varchar(30),
content varchar(512),
time datetime,
address varchar(128),
user_id int,
foreign key (user_id) references user(id)
);

点赞评论
create table user_pyq(
id int primary key auto_increment,
u_id int,
p_id int,
comment varchar(512),
`like` bit,
foreign key (u_id) references user(id),
foreign key (p_id) references pyq(id)
);

综合查询练习
1. 查询每位老师教授的课程数量

select teacher.tname,count(course.teacher_id)
from teacher left join course
on teacher.tid = course.teacher_id
group by teacher.tname;

2. 查询学生的信息及学生所在班级信息
select sid,sname,gender,caption
from student left join class
on student.class_id = class.cid;

3. 查询各科成绩最高和最低的分数,形式 : 课程ID  课程名称 最高分  最低分
select course.cid as 课程ID,course.cname as 课程名称,
max(number) as 最高分,min(number) as 最低分
from course left join score
on course.cid = score.course_id
group by course.cid,course.cname;


4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select student.sid,student.sname,avg(number)
from student left join score
on student.sid = score.student_id
group by student.sid,student.sname
having avg(number) > 85;


5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
6. 查询各个课程及相应的选修人数








