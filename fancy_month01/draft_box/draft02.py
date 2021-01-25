class Character:
    var = 5
    def __init__(self, name, attack_value, hp):
        self.name = name
        self.attack_value = attack_value
        self.hp = hp

    @property
    def attack_value(self):
        return self.__attack_value
    @attack_value.setter
    def attack_value(self,value):
        if 0 <= value <= 100:
           self.__attack_value=value
        else:
            raise ValueError("atc数据超出０－１００")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp= value
        else:
            raise ValueError("hp数据超出０－１００")


p1 = Character("lzf",15,15)
p1.attack_value=12
print(p1.attack_value)
# print(Character.var)

