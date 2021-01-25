class Enemy:
    def __init__(self,hp=0):
        self.hp = hp#传入实例变量

    @property               #将实例变量设置为私有的属性，重写ｈｐ方法
    def hp(self):
        return self.__hp

    @hp.setter#给这私有属性　安排一个　特定的修改方式
    def hp(self,value):
        if not 0 <= value <= 100:
            raise Exception("血量异常",0 <= value <= 100,value)
        else:
            self.__hp = value

    @hp.getter
    def get_hp(self):
        print("get self")
        return self.__hp



while 1:
    try:
        hp = int(input("输入敌人血量："))
        enemy01 = Enemy(hp)
        print(enemy01.hp)     #这个私有的属性　通过我定义的　方法访问
        break
    except Exception as error:
        print(error.args)