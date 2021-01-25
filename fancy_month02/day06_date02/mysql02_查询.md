# 高级查询

## 基本语句

#### 1. like 模糊

` %`来表示任意0个或多个字符，下划线`_`表示任意一个字符。

```sql
select * from class_1 where name like 'A%';
```

#### 2. as 重命名

给字段或者表重命名(方便阅读结果)

```sql
 select name as 姓名,age as 年龄 from class;
```

#### 3. order by 排序

默认情况***asc表示升序***，***desc表示降序***

```sql
select * from class order by score desc,age;
```

#### 4. limit 限制

select \update\delete\order by\ 的操作数量

```sql
查询班级男生第三名
select * from cls where sex='m' order by score desc limit 1 offset 2;
```

#### 5. union 联合

连接两个以上的 select语句的结果组合到一个结果集合中。多个select语句会删除重复的数据．可以改为　all

```sql
 select * from class where sex='m' UNION ALL select * from class_1 where age > 9;
```

## 流程

### 1.子查询

一个select语句中包含另一个select 查询语句

（即我所查询的表来自另一个查询）

```sql
select name from (select * from class_1 where sex='m') as s where s.score > 90;
```

```sql
	select *  from class where age = (select age from class where name='Tom');
 	select * from class where name in (select name from hobby);
```

注意：

1. 子句结果作为一个值使用时，返回的结果需要一个明确值，不能是多行或者多列。
2. 如果子句结果作为一个集合使用，即where子***句中是in操作***，则结果可以是一个字段的多个记录。

## 2.查询执行流程

```mysql
(5)select DISTINCT <select_list>                    



(1)from <left_table> <join_type> JOIN <right_table> ON <on_predicate>

(2)where <where_predicate>

(3)group by <group_by_specification>

(4)having <having_predicate>





(6)order by <order_by_list>

(7)limit <limit_number>
```

## 聚合

### 1.方法

avg\max\min\sum\count\ (clo)

count(*) 数每一条记录row

方法的输出取决于　在使用其作为分类条件之前　做了什么样的分组操作

### 2. group by分组

```sql
select country,avg(attack) from sanguo 
group by country;

#先导入表，以国家分组，再计算国家平均的攻击力，最后输出字段（列）为　国家　和　国家攻击力平均值
```

```sql
select age,sex,count(*) from class group by age,sex;

＃先导入表　以年龄和性别为列分组　，再计算记录的条数（人数）
```

```sql
select country,count(id) as number from sanguo 
where gender='M' group by country
order by number DESC
limit 2;

＃　先导入表　判断出性别为男性　再以这些男性的国家分组　，以这些记录出现的次数　按照国家为分类　降序排列，最后限制输出为两个，为前两名　
```

### 3.having 分组后的筛选

在group by　后使用having  且可以使用聚合方法作为条件（where不可以）

```sql
select country,avg(attack) from sanguo 
group by country
having avg(attack)>105
order by avg(attack) DESC
limit 2;

#　导入表　以国家分组　选择国家的平均战斗力大于１０５　的几个组　按照其平均战斗力降序排列　取前二，输出　列为国家和国家平均战斗力的表格
```

### 4.distinct 去重

```sql
  select distinct name,country from sanguo;
  select count(distinct country) from sanguo;
```



## 列表索引

索引是对数据库表中一列或多列的值进行排序的一种结构，使用索引可快速访问数据库表中的特定信息。

通常我们只在经常进行查询操作的字段上创建索引

### 1.索引分类

MUL 普通索引，字段值无约束,KEY= MUL

UNI 唯一索引，字段值不允许重复,但可为 NULL,KEY=UNI

PRI 主键索引，一个表中只能有一个主键字段, 主键字段不允许重复,且不能为NULL，KEY=PRI。通常设置记录编号字段id,能唯一锁定一条记录

### 2.索引操作

```sql
create table 表名(
字段名 数据类型，
字段名 数据类型，
index 索引名(字段名),
index 索引名(字段名),
unique 索引名(字段名)
);
create [unique] index 索引名 on 表名(字段名);

#主键加索引
alter table 表名 add primary key(id);

#查看索引
1、desc 表名;  --> KEY标志为：MUL 、UNI。
2、show index from 表名;


drop index 索引名 on 表名;
alter table 表名 drop primary key;  # 删除主键


set  profiling = 1； 打开功能 （项目上线一般不打开）
show profiles  查看语句执行信息
```

mysql的key和index多少有点令人迷惑，这实际上考察对数据库体系结构的了解的。

 key
 是数据库的物理结构，它包含两层意义，一是约束（偏重于约束和规范数据库的结构完整性），二是索引（辅助查询用的）。包括primary key, unique key, foreign key 等。

 primary key 
有两个作用，一是约束作用（constraint），用来规范一个存储主键和唯一性，但同时也在此key上建立了一个index；

unique key
 也有两个作用，一是约束作用（constraint），规范数据的唯一性，但同时也在这个key上建立了一个index；

 foreign key
也有两个作用，一是约束作用（constraint），规范数据的引用完整性，但同时也在这个key上建立了一个index；

 可见，mysql的key是同时具有constraint和index的意义，这点和其他数据库表现的可能有区别。（至少在oracle上建立外键，不会自动建立index），



因此创建key也有如下几种方式：
 （1）在字段级以key方式建立， 如 create table t (id int not null primary key);
 （2）在表级以constraint方式建立，如create table t(id int, CONSTRAINT pk_t_id PRIMARY key (id));
 （3）在表级以key方式建立，如create table t(id int, primary key (id));

 其它key创建类似，但不管那种方式，既建立了constraint，又建立了index，只不过index使用的就是这个constraint或key。

2 index
是数据库的物理结构，它只是辅助查询的，它创建时会在另外的表空间（mysql中的innodb表空间）以一个类似目录的结构存储。索引要分类的话，分为前缀索引、全文本索引等；
 因此，索引只是索引，它不会去约束索引的字段的行为（那是key要做的事情）。
 如，create table t(id int, index inx_tx_id (id));



3 最后的释疑：
 （1）我们说索引分类，分为主键索引、唯一索引、普通索引(这才是纯粹的index)等，也是基于是不是把index看作了key。
 比如 create table t(id int, unique index inx_tx_id (id)); --index当作了key使用

 （2）最重要的也就是，不管如何描述，理解index是纯粹的index，还是被当作key，当作key时则会有两种意义或起两种作用。