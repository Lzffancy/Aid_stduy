# 网络基础

## 1.网络简述

* 网络 : 计算机网络功能主要包括实现资源共享，实现数据信息的快速传递。

* 网络协议：在网络数据传输中，都遵循的执行规则,规范

* C/S

  服务器(Server)  向客户端提供资源，保存客户端数据，处理客户端请求等。

  客户端(Client)  收集客户请求,提交给服务器

## 2. OSI 6

## (Open System Interconnection Reference Model)

​     7 Application  各种应用
​     6 Presentation   数据格式化,加密,压缩解压  (数据处理)
​     5  Session  建立,管理,终止 引用之间的会话连接 (会话)
​     
​     4 Transport  提供端到端的服务(UDP/TCP)
​     3  Network  逻辑寻址,路由选择 IP
​     2 DataLink  将数据封装成帧
​     1 Physical   介质上传输比特bit ,提供物理的实现

```
面试:
1.这是什么?  
2.具体描述   
3.特点(优点,缺点)   
4.话题引申  (tcp/ip4)
5.我用它做过什么
(自己不熟悉的技术不多聊,会就会,不会就不会)
```

## 3. TCP/IP 4 

  765 应用层  Telnet(远程) FTP(文件传输) SMTP(邮件传输)
                      DNS (域名服务器) HTTP(超文本传输协议) 



  4 传输层  TCP(传输控制协议,流式),UDP(用户数据报协议,包式) 

  3 网络层 IP(互联网协议地址) ,ARP(地址解析协议),RARP(反向地址          解析协议) ,ICMP(控制报文协议)

```
应用层工程师的工作:
    1.编写应用功能(功能实现)
    2.明确对方地址(IP地址)
    3.选择传输服务(配置好传输层所认可的TCP或UDP)
```





## 4.网络地址 

通信地址 = IP + port
### 4.1 IP
 即在网络中标识一台计算机的地址编号。
(在同一网段下唯一)

IPv4 ： 192.168.1.5     (0-255
IPv6 ：fe80::80a:76cf:ab11:2d73  (4个16进制数

公网IP,互联网上的公共IP地址
内网IP,局域网络内由网络设备分配的IP地址。

### 4.2 port

根据TCP/IP 协议 其首部分配了16位来填写端口
所以 2^16即为65535
0-1023 为系统占用
1024-65535 为用户使用



# Socket in py

* 套接字(Socket) ： 实现网络编程进行数据传输的一种技术手段,
* 套接字***上联应用进程，下联网络协议栈***，(中间虚拟层)是应用程序通过***网络协议***进行***通信***的***接口***，是应用程序与***网络协议根***进行交互的接口
* 允许数据丢失

相当于在  765 应用层 与 4 传输层 之间添加了一个Socket抽象层,Socket其实就是一个门面模式，***它把复杂的TCP/IP协议族隐藏在Socket接口后面，***对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。



## 1. UDP socket

User Data Protocol，用户数据报协议

```python
#server
from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
#返回值： 套接字对象

#服务器绑定地址
addr = ('0.0.0.0',8888)
sockfd.bind()

#消息收发
data,addr = sockfd.recvfrom(buffersize)
    功能： 接收UDP消息(堵塞函数)
    参数： 每次最多接收多少字节
    返回值：addr  消息发送方地址
    
n = sockfd.sendto(data,addr)
    功能： 发送UDP消息
    参数： data  发送的内容 #bytes格式
          addr  目标地址
    返回值：发送的字节数
#关闭socket
  sockfd.close()
```

udp特点

* 可能会出现数据丢失的情况
* 传输过程简单，实现容易
* 数据以数据包形式表达传输
* 数据传输效率较高
  

## 2. TCP socket

Transmission Control Protocol  传输控制协议 

```python
#server
from socket import *
#抽象socket层
sockfd=socket(AF_INET,SOCK_STREAM)
#服务器绑定地址
addr = ('0.0.0.0',8888)
sockfd.bind()
#确定监听队列大小
#一个listen最多连接1024个
sockfd.listen(n)
#－－－－－－－－－－－－－－－－－－－－－－－－－
#socket重生成客户端 连接套接字
#阻塞等待处理客户端connect请求
connfd,addr = sockfd.accept()

#消息收发
data,addr = connfd.recv(buffersize)
n = connfd.send(data,addr)

#关闭socket
connfd.close()
sockfd.close()

#fd file descriptior 文件描述符
```

```python
#client
class Dialog_client():
    # 初始化配置客户端,连接服务器
    def __init__(self):
        self.S_ADDR = ('127.0.0.1', 65534)
        self.socket_c = socket(AF_INET, SOCK_STREAM)
        
    # 收集用户消息,发送给服务器,再接收服务器回消息
    def sent_req(self):
        req_input = input("你想问什么?")
       #tcp需要建立连接,socket.connect(s_addr)
       self.socket_c.connect(self.S_ADDR)
       self.socket_c.send(req_input.encode())
        
        answer = self.socket_c.recv(1024)
        print(answer.decode())
        self.socket_c.close()

```



###　2.1 TCP 流程
三次握手,四次挥手

* 建立连接

  1. client－－>  server
      SYN=1 ;seq = x

  2. client   < －－server
     SYN=1 ;ACK =1;ack = x+1;seq = y

  3. client －－>   server

  ​       ACK=1 ;ack = y+1

  --------------------------------------------------------------------------

  

* 断开连接(CS端都可以发起)

  1. client－－>  server
     FIN=1 ;seq = x

  2. client   < －－server
     ACK=1;ack=x+1; seq=y

  3. client   < －－server

     FIN=1;ACK=1;ack = x+1;seq =z

  4. client－－>  server

     ACK=1;ack=z+1;seq=h

### 2.2 标志含义

* *SYN(synchronization) 发起同步标志*
  SYN=1,ACK=0 为发起连接方
  SYN=1,ACK=1 连接方同意连接

  

* ACK(acknowledgment) 接收标志
  连接建立后所有的传送的报文段都必须把ACK置为1

  

* FIN(finish) 释放连接标志
  双方互发FIN=1,则连接将要被释放

* seq(sequence) 序号

  TCP是面向字节流的。在一个TCP连接中传送的字节流中的每一个字节都按顺序编号。

  ```
  例如，一报文段的序号是301，而接待的数据共有100字节。这就表明本报文段的数据的第一个字节的序号是301，最后一个字节的序号是400。
  ```

* ack(acknowledgment) 确认号
  期望收到对方下一个报文段的第一个数据字节的序号seq+1

```
比如第一次发送端传送数据seq=1，发送数据725byte，则下一次发送端的seq为726))

ack取决于发送过来数据的大小 比如初始发送了42byte，此时回送的ack为43（表示<43的数据已全部确认(累积确认)期望收到序号为43的包)
```

### 2.3 TCP socket细节

#### 2.3.1 异常断开

* tcp连接中当一端退出，另一端如果阻塞在recv，此时recv会立即返回***一个***空字串。

* tcp连接中如果一端已经不存在，仍然试图通过send向其发送数据则会产生BrokenPipeError.

* 一个服务端可以同时连接多个客户端，也能够重复被连接(建立连接一次断开，短连接）

  

#### 2.3.2 TCP粘包问题
发的快，读的慢，存在系统缓存区

原因：1.操作系统设置了缓冲区
　　　2.导致消息收发速度不一致
           3.字节流方式,不区分消息边界

影响:   如果***每次发送内容是一个独立的含义***，需要接收端独立解析,此事粘包导致含义混合．

解决：　1.消息格式化处理，添加消息边界
　　　　 2.*控制发送的速度*



# 数据传输流程

1.程序发送消息，***逐层添加首部***信息，最终在物理层发送***消息包***。

2.发送的消息经过多个节点（交换机，路由器）传输，最终到达目标主机。

3.目标主机由物理层逐层解析***首部消息包***，最终到应用程序呈现消息

![](/home/tarena/桌面/fancy_month02/day10_udp/14.png)









