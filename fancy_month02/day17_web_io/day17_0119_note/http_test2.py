"""
http请求和响应

"""
from socket import *

ADDR = (("0.0.0.0", 65530))


def server_ready():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(20)
print("listen....")


def handle():
    pass


# 等待浏览器连接
connfd, addr = sock.accept()
print("connect from", addr)

request = connfd.recv(1024 * 1024)
print(request.decode())
html_file = open('my_bing.html', 'rb')
html_data = html_file.read()

response = """
HTTP/1.1 200 OK
Content-Type: text/html    

%s 
           """ % html_data
connfd.send(response.encode())
