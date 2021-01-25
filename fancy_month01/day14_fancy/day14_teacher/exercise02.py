"""
   创建敌人类,限制敌人血量在0--100之间
   如果数据超过范围,重新创建敌人对象.
"""


class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise Exception("血量超过范围", 1001, "if 0 <= value <= 100")


while True:
    try:
        hp = int(input("请输入血量:"))
        w01 = Enemy(hp)
        print(w01.hp)
        break
    except Exception as e:
        print(e.args)
