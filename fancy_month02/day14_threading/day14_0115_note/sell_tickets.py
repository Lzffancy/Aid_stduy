"模拟卖票买票"

from threading import Thread,Lock
from time import sleep
#　线程争夺贡献资源，无序使用，可能造成列表已空，但仍有线程去pop列表
tik_source = ["ticket %d"%t for t in range(1,100001)]
lock = Lock()
def sell_tickets(windows):
    """
    :param get_tk:
    :return:
    """

    global tik_source

    while tik_source:
     #print(tik_source)
     #sleep(0.1)
     sent_tik = tik_source.pop()
     sleep(0.02) #加阻塞
     print("窗口%s--->出票%s,成功"%(windows,sent_tik))


def thr10_get_tik():
    for i  in range(1,11):
        t = Thread(target=sell_tickets,args=(i,))
        t.start()




if __name__ == '__main__':
    thr10_get_tik()