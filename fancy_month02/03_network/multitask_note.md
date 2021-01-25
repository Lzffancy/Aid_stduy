# what is multitask ?

## 1.原理

***轮询机制***（Polling）： cpu都在多个任务之间快速的切换执行，切换速度在微秒级别，***其实cpu同时只执行一个任务***，但是因为切换太快了，从应用层看好像所有任务同时在执行。

多核CPU：现在的计算机一般都是多核CPU，多个单核CPU的集合。这，也可以将多个任务分配给多个cpu核心，操作系统会自动根据任务的复杂程度选择最优的分配方案。

## 2.实现（顺序，并行，并发）

实现多任务编程的方法 ： **多进程编程（multiprocess)，多线程编程(multithread)**

* 在任务中***无阻塞***时只有***并行***状态才能***提高效率***

![17](I:\AID2011\fancy_month02\03_network\note_img\17.jpg)



在任务中***有阻塞******时并行并发都***能提高效率
但并发能更加有效的利用cpu资源

![18](I:\AID2011\fancy_month02\03_network\note_img\18.jpg)

# Multi_Process in py

*  进程：***程序在计算机中的一次执行过程。*** 
          是一种动态的过程描述，将占用计算机资源 ；

* 程序：可执行文件； 静态占有磁盘

## 1.进程五态

![4_5](I:\AID2011\fancy_month02\03_network\note_img\4_5.png)

新建：***创建***进程，获取建立进程所需的资源

就绪： 进程具备执行条件，***等待***系统调度分配cpu资源等

执行：进程占用cup资源等，正在***运行***

等待：进程***内部阻塞***，出让cup等资源

终止：进程结束，***释放占用***的所有资源



## 2.进程树

```shell
ps -aux
```

* * USER ： 进程的创建者
  * PID  :  操作系统分配给进程的编号
  * %CPU,%MEM : 占有的CPU和内存
  * STAT ： 进程状态信息，S I 表示阻塞状态 （  应用阻塞S，系统阻塞I） ，R 表示***就绪***状态或者***运行***状态
  * COMMAND : 通过什么程序启动的进程

```shell
pstree
```

父子进程：在Linux操作系统中，进程形成树形关系，任务上一级进程是下一级的***父进程***，下一级进程是上一级的***子进程***。



## 3.multiprocessing.py

### 3.1 Process
​    1.通过模块的Process类创建进程对象，关联需要新进程执行的函数

​    2.通过进程对象调用start启动进程
​       在p.start()后，子进程***复制原有父进程所有存储空间***，但***只执行***绑定target的函数

```python
from multiprocessing import Process
def a():
    print("我想成为子进程")
p= Process(target =a) #用类去 实例化进程对象。此处传参给a,可以填args=,kwargs=,（位置元组，关键字字典）
p.start()  #此时新进程才被真正创建


"""
  p.join（）　 父亲先结束，等待子
  daemon=1 父亲先结束，立刻结束子
"""
```

  p.join（20）　 父亲先结束，**等待子**，（20秒
  daemon=True 父亲先结束，***立刻结束子***

***注意***

* 新进程是原有进程的子进程，一个进程可以创建多个子进程。
* ***子进程只执行指定的函数***，***拥有其他父进程资源。***
* 各个进程在执行上互不影响，也没有先后顺序关系。
  进程创建后，各个进程空间独立，相互没有影响。
  （从时间上来说，父进程先执行到p.start()后子进程开始执行，此时父子进程在占用系统资源的地位是平级的。）
* multiprocessing 创建的子进程中无法使用标准输入（即无法使用input）

```python
#cookie : 使用windows macOS,在main后执行子进程
if __name__ == '__main__'
process = mp.Process(target= fun)
process.start() 
process.join()
```

### 3.2 class process

```python
from multiprocessing import Process
class My_process(Process)
      def __init__(self,a=1):
        self.a= a
        super().__init__()  #继承父类实例变量
       # 重写父类 方法，使用start()触发
      def run(self):
        print('子进程',self.a)
        
p = My_process(a)
p.start()
```

### 3.3 Queue

进程间空间独立，资源不共享，依赖第三个空间进行通信

通信方法：消息队列，***套接字***等。

```python
from multiprocessing import Queue
q = Queue(maxsize=0)
参数：最多存放消息个数

q.put(data)
参数：data  要存入的内容（存满了会阻塞）
q.get()
返回值： 返回获取到的内容（读空了会阻塞）

q.full()   判断队列是否为满
q.empty()  判断队列是否为空
q.qsize()  获取队列中消息个数
q.close()  关闭队列

#消息队列在父进程中创建
#先进先出，排队
```

### 3.4 Pool

进程池
1.进程的创建和销毁过程消耗的资源较多

2.当任务量众多，每个任务在很短时间内完成时，需要频繁的创建和销毁进程。此时对计算机压力较大

原理 (***进程复用***)
***创建一定数量的进程***来处理事件，事件处理完进程***不退出***而是继续处理其他事件，直到所有事件***全都处理完毕统一销毁***。
增加***进程的重复利用***，降低资源消耗。

```python
    from multiprocessing import Pool

     pool = Pool(processes)
    功能： 创建进程池对象
    参数： 指定进程数量，默认根据系统自动判定
      
     pool.apply_async(func,args,kwds)
    功能: 使用进程池执行 func事件
    参数： func 事件函数
          args 元组  给func按位置传参
          kwds 字典  给func按照键值传参
    
     pool.close()
    功能： 关闭进程池
     pool.join()
    功能： 回收进程池中进程
    
```

# Multi_Thread

```python
'''
线程被称为***轻量级的进程***，也是多任务编程方式,利用计算机的多cpu资源。
即在进程中再开辟的分支任务
'''
```

## 1.**特征**

* 线程也是一个运行行为，消耗计算机资源
* ***共享这个进程的资源***
* 线程之间互不影响各自运行
* 创建和销毁***消耗资源远小于***进程

![21](I:\AID2011\fancy_month02\03_network\note_img\21.jpg)

![22](I:\AID2011\fancy_month02\03_network\note_img\22.jpg)

    进程是一类系统资源占用的活动 
    main算一个线程，进程＝main线程+线程ｘ
　线程占用进程内存空间（非完全独立，只执行单一功能

## 2.threading

### 2.1 Thread

```python
from threading import Thread 
t = Thread()
t.start()
t.join([timeout])
#参照process
```

### 2.2 class thread 

```python
from threading import Thread
class My_thread(Thread)
     def __init__(self) 
      ...
         super.()__init__()
     def run(self)
      ...
#参照process
```

* 线程通信方法： ***线程间***使用***全局变量***进行通信


### 2.3 线程同步互斥

同步 ： 同步是一种协作关系，按照必要的步骤有序执行操作。
            A -B -A -B -A-B

互斥 ： 互斥是一种制约关系，当一个进程或者线程占有资源时会进行***加锁处理***，抢相同资源



### 2.4 Event

```python
from threading import Event

e = Event()  创建线程event对象   #（unset）

e.wait([timeout])  阻塞等待e被set  # unset则阻塞，(set)则放行

e.set()  设置e，使wait结束阻塞    #(set)

e.clear() 使e回到未被设置状态　　　#（unset）

e.is_set()  查看当前e是否被设置
```

![event](I:\AID2011\fancy_month02\03_network\note_img\event.png)

### 2.5 Lock

```python
from  threading import Lock
lock = Lock()  创建锁对象

lock.acquire() 上锁  #如果lock已经上锁再调用也会阻塞
lock.release() 解锁
```

#### 2.5.1 Dead lock

* 死锁产生条件

  * 互斥条件：指线程使用了互斥方法，使用一个资源时其他线程无法使用。
  * ***请求***和***保持***条件：指线程已经***保持***至少***一个资源***，但又提出了***新的资源请***求，在获取到新的资源前***不会释放自己保持的资源***。
  * 不剥夺条件：不会受到线程外部的干扰，如系统强制终止线程等。
  * 环路等待条件：指在发生死锁时，必然存在一个***线程——资源的环形链***，如 T0正在等待一个T1占用的资源；T1正在等待T2占用的资源，……，Tn正在等待已被T0占用的资源。




* 如何避免死锁

  * ***逻辑清晰***，不要同时出现上述死锁产生的四个条件
  * 通过测试工程师进行死锁检测

  

#### 2.5.2 GIL

（全局解释器锁）***对线程的影响***

python解释器设计中加入了解释器锁
导致python解释器***同一时刻只能解释执行一个线程***(轮询），大大降低了***线程***的执行效率。（只能是并发）

因为遇到阻塞时线程会主动让出解释器，去解释其他线程。
所以python***多线程***在***执行多阻塞任务***时可以提升程序效率，其他情况并不能对效率有所提升。

在***无阻塞状态下***，***多线程 程序执行效率并不高***，甚至还不如单线程效率。

***Python多线程只适用于执行有阻塞延迟***的任务情形。

```python
#解决方案

* 尽量使用''进程''完成无阻塞的并发行为

* 不使用c作为解释器 （可以用Java  C#）

 Guido的声明：<http://www.artima.com/forums/flat.jsp?forum=106&thread=214235>
```



# process & thread 小结

### 1.区别联系

1. 两者都是多任务编程方式，都能使用计算机多核资源

2. ***进程***的创建删除***消耗的计算机资源***比线程多

   

3. 进程空间独立，数据互不干扰，有专门通信方法 (queue)
   线程使用全局变量通信  (global)

4. 多个线程共享进程资源，操作时往往需要同步互斥处理(lock)

   

5. 一个进程可以有多个分支线程，两者有包含关系

6. Python线程存在***GIL问题***，但是***进程没有***。
   

### 2.使用场景


1. 任务场景：一个大型服务，往往包含多个独立的任务模块，每个任务模块又有多个小独立任务构成，此时***整个项目***可能有***多个进程***，***每个进程***又有***多个线程***。

2. 编程语言：***Java,C#之类***的编程语言在执行多任务时一般都是***用线程完成***，因为线程资源消耗少；

   而***Python***由于GIL问题***往往使用多进程***
   
   
   
   
   
### 3.进程相关函数

   ```python
   import sys,os
   os.getpid()   #返回值： 返回当前进程的PID 
   os.getppid()  #返回值： 返回父进程PID
   sys.exit(info)#功能：退出进程 表示退出时打印内容
   ```


```fancy
date 2021.1.16
```

