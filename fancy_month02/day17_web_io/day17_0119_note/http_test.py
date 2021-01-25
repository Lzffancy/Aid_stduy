"""
http请求和响应

"""
from  socket import *
addr =(("0.0.0.0",65530))


sock = socket(AF_INET,SOCK_STREAM)
sock.bind(addr)

sock.listen(20)
print("listen....")

#等待浏览器连接
connfd,addr =sock.accept()
print("connect from",addr)

request = connfd.recv(1024*1024)
print(request.decode())
html_file = open('my_bing.html','rb')
html_data=html_file.read()

response = """
HTTP/1.1 200 OK
Content-Type: text/html    

%s 
           """%html_data
connfd.send(response.encode())
html_file.close()
