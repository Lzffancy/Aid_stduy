## １.外键foreign key

***（当出现一对多的逻辑时）***，外键值为多的那一侧

约束，对从表字段约束

foreign key 建立主从表关系，从表外键　链接主表主键（一般）
foreign key 外键的定义语法：

#### 1.1建立外键

建表时：

```sql
[constraint symbol] foreign key（子表外键字段） 
references tbl_name (主表主键)
[on delete {restrict | casecade | set null | no action}]
[on update ...]
```

建表后：

```sql
alter table person add 
foreign key(dept_id) 
references dept(id);
```

　注意：从表的外键字段数据类型与指定的主表主键应该相同。

　constraint 可自定义外键关系的名称

  　联级动作　主表动　从表不动，跟随，或置null

* restrict(默认)  :  on delete restrict  on update restrict　＃无联级
* cascade ：  on delete cascade   on update cascade　＃***数据级联更新***
* set null  :   on delete set null　on update set null　＃联级删除,更新为null

#### 1.2解除外键

```sql
alter table person drop foreign key dept_fk;
# 查看外键名称
show create table person;
```

#### 1.3表关联关系

***一对多和多对多是常见的表数据关系***：

* 一对多，一张主表一张从表

* 多对多，两张主表一张关系从表

  从表一般带有不完整信息，需要主表(primary key id)作为补充

1.4 E-R模型

　　　Entry-Relationship

　　	实体 row　　　　矩形框

　　　属性　column　　椭圆

　　　关系　表关联 　　菱形框

## 2.联合查询

***外键约束之间并没有必然联系***，但是基于外键约束设计的具有关联性的表往往会更多使用关联查询查找数据。

内连接　inner

左连接    left      左表全部显示，显示右表中与左表匹配的项

```sql
select * from person left join  dept  
on  person.dept_id =dept.id;
```

***注意：我们尽量使用数据量大的表作为基准表,放在前面，然后使用左连接．***

#### 逻辑：

```sql
7.查询每位学生的姓名，班级　和各科平均分
select sname,caption,avg(number) 
from student left join class
on student.class_id  =  class.cid
left join score
on student.sid = score.student_id
group by sname,caption;

6. 查询各个课程及相应的选修人数
select course.cname,count(score.student_id)
from course left join score
on course.cid = score.course_id
group by  course.cname;
```

select  6.(需要展示的字段，这些字段是否需要使用函数？)

 from    1.(数据来自哪个几个表　链接　需要的数据？) 
　on    2.(需要建立什么样的链接　，主表主键＝从表外键)
where  3.(确定条件的判断)

group by 4.(分组)
having     5.(需要使用函数的判断)

## 3. view 视图

  存储的查询语句,产生结果集,视图是***虚拟表***,可以分配给其他用户使用

 不额外占用空间，***绑定原数据表***,***视图的增删改查操作与一般表的操作相同（数据只有一份，同时改变***）

#### 3.1操作view

```sql
语法结构：
create [or replace] view [view_name]as[select_statement]
```

* 视图增删改查，使用insert update delete select

* 查看现有view

  ```sql
  show full tables in stu where table_type like 'VIEW';
  ```


* drop view [if exists] 视图名

* 修改视图

  参考创建视图，将create关键字改为alter

## 4.函数和过程

​       ***定义:一段sql语句集合***

#### 4.1 function

（函数：实现一定功能的语句的封装集合）
  创建函数

```sql
delimiter //
create function a_b_score(name1 varchar(10),name2 varchar(10))
returns int
begin
   declare num1 int;
   declare num2 int;
  set num1 = (select score from class where name=name1);
  select score from class where name=name2 into num2;
   return num1 - num2;
end//
delimiter ;

select a_b_score('fancy','tom')
```

设置变量

* 定义用户变量 ： set  @[变量名] = 值；

  ​                            使用时用@[变量名]。

  

* 定义局部变量 ： 在函数内部设置:  declare   [变量名]    [变量类型];                                              

  ​                            局部变量:    set赋值或者使用into关键字

#### 4.2 procedure

```sql
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
```

存储过程三个参数的区别

* in 类型参数可以接收***变量***也可以***接收常量***，传入的参数在存储过程内部***使用***即可，但是在存储过程内部的修改无法传递到外部。
* out 类型参数只能接收一个***变量***，接收的变量不能够在存储过程内部使用（***内部为NULL***），但是可以***在存储过程内对这个变量进行修改***。因为定义的变量是全局的，所以外部可以获取这个修改后的值。
* input 类型参数同样只能接收一个***变量***，但是这个变量可以在存储过程***内部使用***。在存储过程内部的***修改也会传递到外部***。



#### 4.3 查看

```sql
show create  {procedure|function}  存储过程或存储函数的名称
select name,type from mysql.proc where db='stu';
DROP {PROCEDURE | FUNCTION} [IF EXISTS] pf_name
```



#### 4.4 区别和特点

1.function 只有一个返回值;普通参数;select 调用
   procedure 无返回值; in out inout 类型;call 调用

2.functon 函数中不能展示查询结果集,语句完成查询的工作后返回一个结果，功能针对性比较强。
  procedure 理解为一个按照预定步骤调用的执行过程



## 5.事物控制 transaction control
主要处理数据的增删改操作,确保数据操作过程中的***数据完整***和***使用安全***。

```sql
mysql>begin; 
(sql 语句)
(sql 语句)
(sql 语句)
mysql>commit; # 事务中SQL命令都执行成功,提交到数据库,结束!
(or)
mysql>rollback; # 有SQL命令执行失败,回滚到初始状态,结束!
   
# 注意：事务操作只针对数据操作。rollback不能对数据库，数据表结构操作恢复。
```



#### 5.1 ACID

1.原子性（atomicity）
所有操作要么全部提交成功，要么全部失败回滚

2.一致性（consistency）
事务完成时，数据必须处于一致状态，数据的完整性约束没有被破坏。

3.隔离性（isolation）
防止多个事务并发执行时由于***交叉执行***而导致数据的不一致。

4.持久性（durability）
事务提交，则其所做的修改就会永久保存到数据库中。



#### 5.2 事务隔离级别 isolation

1.读未提交：read uncommitted
***事物A未提交的数据，事物B可以读取到***
这里读取到的数据叫做“脏数据”

2.读已提交：read committed
***事物A提交的数据，事物B才能读取到***
会导致“不可重复读取”

3.可重复读：repeatable read
***MySQL默认级别***
***事务A提交之后的数据，事务B读取不到***
(B读取的是A提交修改之前的数据,不会立即同步给B,但在B进行修改操作的时候,会同步A的修改)
导致“幻像读”

4.串行化：serializable
事务A在操作数据库时，事务B只能排队等待
吞吐量太低，用户体验差



## 6.数据库优化

#### 6.1 范式

***(主要是表的设计)***

> 目前关系数据库有六种范式：第一范式（1NF）、第二范式（2NF）、第三范式（3NF）、巴斯-科德范式（BCNF）、第四范式(4NF）和第五范式（5NF，又称完美范式）。

越高的范式数据库冗余越小。但是***范式越高***也意味着***表***的划分更***细***，一个数据库中需要的***表也就越多***,***常数据库设计遵循第一第二第三范式***

* 第一范式  colums 为原子数据项
* 第二范式 ***实例***或 row 可以被唯一的区分,所有***属性（columns)***依赖于***主属性(primary key)***。(设置主键)
* 第三范式 属性不传递依赖</u>,***合理使用外键(forieger key)***，***(外键尽量连接主键***）使不同的表中不要有重复的字段.



#### 6.2 引擎

mysql数据库管理系统中用来处理表的处理器

***基本操作***

```sql
1、查看所有存储引擎
   mysql> show engines;
2、查看已有表的存储引擎
   mysql> show create table 表名;
3、创建表指定
   create table 表名(...)engine=MyISAM;
4、已有表指定
   alter table 表名 engine=InnoDB;
```

* **InnoDB**	(对写操作友好)

  ```
  1. 支持行级锁
  2. 支持外键、事务、事务回滚
  3. 表字段和索引同存储在一个文件中
  		 1. 表名.frm ：表结构
   		 2. 表名.ibd : 表记录及索引文件
   		 
  注意 Innodb如果不设置主键也会自己设置隐含的主键
  ```

* **MyISAM**　（查操作友好）

```
1. 支持表级锁
2. 表字段和索引分开存储
      	 1. 表名.frm ：表结构
         2. 表名.MYI : 索引文件(my index)
         3. 表名.MYD : 表记录(my data)
```

#### 6.3 数据类型选择

- 数据类型优先程度  

   数字类型 -->  时间日期类型  --> 字符串类型

- 同一级别  

-  占用空间小的 --> 占用空间大的

```
字符串在查询比较排序时数据处理慢
占用空间少，数据库占磁盘页少，读写处理就更快
```

Tips:

1. Innodb如果不设置主键也会自己设置隐含的主键，所以***最好自己设置***

2. 尽量设置占用空间小的字段为主键

3. 建立外键会自动建立索引，在表***关联查询***时建议使用**外键字段**作为关联条件
   (外键虽然可以保持数据完整性，但是会降低数据导入和操作效率，增加维护成本)

#### 6.4 SQL语句优化

通过explain命令可以得到:
知道MySQL是如何处理你的SQL语句的

-  表的读取顺序
-  数据读取操作的操作类型
-  哪些索引可以使用
-  哪些索引被实际使用
-  表之间的引用
-  每张表有多少行被优化器查询

```sql
explain select * from class where id <5;
```



***EXPLAIN主要字段解析***：

* table：显示这一行的数据是关于哪张表的
  
* type：这是最重要的字段之一，显示查询使用了何种类型。从最好到最差的连接类型为
  system、const、eq_reg、ref、range、index和ALL，
  一般来说，***得保证查询至少达到range级别***，最好能达到ref。(通过索引访问提高效率)

```
type中包含的值：
- system、co　nst： 可以将查询的变量转为常量. 如id=1; id为 主键或唯一键.
- eq_ref： 访问索引,返回某单一行的数据.(通常在联接时出现，查询使用的索引为主键或唯一键)
- ref： 访问索引,返回某个值的数据.(可以返回多行) 通常使用=时发生 
- range： 这个连接类型使用索引返回一个范围中的行，比如使用>或<查找东西，并且该字段上建有索引时发生的情况
- index： 以索引的顺序进行全表扫描，优点是不用排序,缺点是还要全表扫描 
- ALL： 全表扫描，应该尽量避免
```

* possible_keys：显示可能应用在这张表中的索引。如果为空，表示没有可能应用的索引。

* key：实际使用的索引。如果为NULL，则没有使用索引。

* key_len：使用的索引的长度。在不损失精确性的情况下，长度越短越好

* rows：MySQL认为必须检索的用来返回请求数据的行数

#### 6.5 优化小提示

1.选择占用空间小,在where,group by ,order by,中出现频率高的字段建立索引

2.避免使用 select * ,不返回不需要用到的字段

3.查询后添加limit 来停止扫描

4.避免使用null 值做判断(where num is null),默认为空使用默认为0代替(where num=0)

5.避免使用or 连接条件,使用 union all连接两个查询语句
 where id=10 or id=20;
 where id=10 union all  select id from t1 where id=20;

6.避免使用 in ,not in ,可以使用between 代替
where id in (1,2,3,4);
where id between 1 and 4;

## 7. 数据库管理

#### 7.1拆分表

超过500w条row 算大 ,或者50+ column 算大

垂直拆分(column) ：***将常查询的字段放到一起***，(热数据)blob或者text类型字段放到另一个表,(需要建立表关系)

水平拆分(row) ： 减少每个表的数据量，通过关键字进行划分然后拆成多个表

#### 7.2 复制表

```sql
1. 表能根据实际需求复制数据
2. 复制表时不会把KEY属性复制过来

create table 表名 select 查询命令;
```

#### 7.3 备份库

```linux
mysqldump   -u  用户名   -p   源库名  >  ~/stu.sql
mysql   -u  root   -p    目标库名 <  stu.sql
```

7.4 远程连接SQL

```mysql
更改配置文件，重启服务！

1.cd /etc/mysql/mysql.conf.d
2.sudo vi mysqld.cnf  找到43行左右,加 # 注释
   # bind-address = 127.0.0.1
3.保存退出 wq
4.sudo service mysql restart

#---------------------------------------------
5.进入mysql修改用户表host值 
  use mysql;
  update user set host='%' where user='root';
6.刷新权限
  flush privileges;
  
 7.在mysql库下 查看用户
 select host,user from user;


```

7.5 添加用户和授权

```mysql
1. 用root用户登录mysql
   mysql -u root -p
   
2. 添加用户 % 表示自动选择可用IP
   CREATE USER 'username'@'host' IDENTIFIED BY 'password';
   
3. 权限管理

   # 增加权限
   grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
   
    权限列表(all privileges ，select ，insert ，update，delete，alter，create，drop等。
库.表 ： *.* 代表所有库的所有表)
   
   # 删除权限
   revoke insert,update,select on 库.表 from 'user'@'%';
   
4. 刷新权限
   flush privileges;
   
5. 删除用户
   drop user "用户名"@"%"
```

