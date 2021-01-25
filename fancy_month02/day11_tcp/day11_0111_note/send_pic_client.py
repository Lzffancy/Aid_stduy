'''
send file client
You deserve someone who loves you with every beat of his heart.
'''

from socket import *

def send_file(tcp_socket,pic_path):
    with  open(pic_path, 'rb') as pic_file:
        while 1:
            pic_data = pic_file.read(1024)
            if not pic_data:
                break
            tcp_socket.send(pic_data)
    # 发送结束位
        tcp_socket.send(b"##")

    re_msg = tcp_socket.recv(1024)
    print(re_msg.decode())
    #tcp_socket.close()


def main(pic_path):
    S_ADDR = ('127.0.0.1', 65534)
    tcp_socket_c = socket(AF_INET, SOCK_STREAM)
    tcp_socket_c.connect(S_ADDR)

    send_file(tcp_socket_c,pic_path)




if __name__ == '__main__':
    pic_path = '/home/tarena/桌面/share/pic.jpeg'
    main(pic_path)









'''pic_path ='/home/tarena/桌面/share/pic.jpeg'

with  open(pic_path,'rb') as pic_file:
      pic = pic_file.read()
      print(pic)
tcp_sockte_c.send(pic)
re_data= tcp_sockte_c.recv(1024)
print(re_data.decode())
'''
