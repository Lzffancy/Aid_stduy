 book表拆分 为三个表
 图书表
 出版社
 作家表
 设计表关系，根据设计完成表创建

 create table 作家(
 id int primary key auto_increment,
 name varchar(30),
 sex char,
 comment text
 );

 create table 出版社(
 id int primary key auto_increment,
 pname varchar(50),
 address varchar(128),
 tel char(16)
 );

 create table 图书(
 id char(20) primary key,
 bname varchar(30),
 price float,
 author_id int,
 press_id int,
 foreign key (author_id) references 作家(id),
 foreign key (press_id) references 出版社(id)
 );

 create table press_author(
 id int primary key auto_increment,
 author_id int,
 press_id int,
 foreign key (author_id) references 作家(id),
 foreign key (press_id) references 出版社(id)
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
select student.sid,sname from
student left join score
on student.sid = score.student_id
where course_id=2 and number>80;

6. 查询各个课程及相应的选修人数
select cname,count(course_id) from
course left join score
on course.cid = score.course_id
group by cname;

7. 查询每位学生的姓名，所在班级和各科平均分
select sname,caption,avg(number) from
student
left join class
on class.cid = student.class_id
left join score
on student.sid = score.student_id
group by sname,caption;


函数

delimiter $$

create function st() returns int
begin
    update class set score=99 where id=1;
    delete from class where sex is null;
    return (select age from class where name="Joy");
end $$

delimiter ;

局部变量
delimiter $$

create function st4() returns int
begin
    declare num_1 int;
    declare num_2 int;
    set num_1=(select score from class order by score desc limit 1);
    select score from class order by score limit 1 into num_2;
    return num_1-num_2;
end $$

delimiter ;

练习：
编写一个函数，传入两个学生的名字，得到两个
学生的分数之差

delimiter $$
create function queryScore(name1 varchar(30),name2 varchar(30))
returns float
begin
    declare val1 float;
    declare val2 float;
    set val1=(select score from class where name=name1);
    set val2=(select score from class where name=name2);
    return val1-val2;
end $$
delimiter ;


create procedure p_out ( out num int )
begin
    select num;
    set num=100;
    select num;
end $$

set @a=10;
call p_out(@a)

练习
编写一个存储过程，传入一个ID，删除该ID学生信息
将id为1的学生成绩改为100分。

create procedure delete_stu(in uid int)
begin
   delete from class where id=uid;
   update class set score=100 where id=1;
end $$

