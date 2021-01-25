"""
http请求和响应 演示
"""
from socket import *

sock = socket()
sock.bind(("0.0.0.0",8000))
sock.listen(5)

# 等待浏览器连接
connfd,addr = sock.accept()
print("Connect from",addr)

# 接收HTTP请求
request = connfd.recv(1024)
print(request.decode())

# 组织响应
response = """HTTP/1.1 200 OK
Content-Type:text/html

hello world
"""
connfd.send(response.encode())

connfd.close()
sock.close()
