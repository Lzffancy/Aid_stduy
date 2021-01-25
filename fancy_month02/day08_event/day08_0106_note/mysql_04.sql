select sname,caption,avg(number) from
student left join class
on student.class_id  =  class.cid
left join score
on student.sid = score.student_id
group by sname;

create view good_stu as select id,name,age,score
from class
where score>85;



select * from good_stu order by score;

create [or replace] view stu_hobby as select class.name,age,hobby,price
from class,hobby
where class.name = hobby.name;

#-----------------------------------------
show full tables in fancy_personal
where table_type like 'view';

alter view good_stu
as select name,age,score
from class
where score > 70;


create or replace view  xxx as select


drop view if exists stu_hobby;


#function-----------------------------
delimiter //
create function  st2() returns int
begin
  return (select age from class where name='fancy');
end//

delimiter ;

#---------------
delimiter //
create function st4() returns int
begin
    declare num1 int;
    declare num2 int;
    set num1 =(select score from class order by score desc limit 1);
    select score from class order by score asc limit 1 into num2;
    return num1 - num2;
end //
delimiter ;


delimiter //
create  function  qnbid(uid int)
returns varchar(20)
begin
return (select name from class where id=uid);
end //
delimiter;
#----------------------------------------------
delimiter //
create function a_b_score(name1 varchar(10),name2 varchar(10))
returns int
begin
   declare num1 int;
   declare num2 int;
   set num1 = (select score from class where name=name1);
   set num2 = (select score from class where name=name2);
   return num1 - num2;
end//
delimiter ;


#--------------------------存储过程

delimiter //
create procedure st()
begin
  select name,age from class;
  select name,score from class order by score desc;
end//
delimiter ;

call st();


#------------------------------------


delimiter //
create procedure p_out (out num int)
begin
  select num;
  set num = 100;
  select num;
end//
delimiter ;

set @var_num =10;
call p_out(@var_num);
select @var_num;


#-------------------------------------
delimiter //
create  procedure p_del_update(in uid01 int)
begin
   delete from class where uid01 =ID;
   update class set score = 100 where ID=2;
end //
delimiter ;

#----------------------------------------------
select name,type from mysql.proc where db='fancy_personal';
#----------------------------------------------
alter table hobby engine=myisam;

