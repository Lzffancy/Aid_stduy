"""
    封装：创建玩家/敌人类
    继承：创建角色类,隔离玩家与敌人
    多态：具体角色(玩家/敌人)攻击时调用角色类
         具体角色重写角色的受伤(damage)方法
         创建玩家与敌人对象
    目的:增加新具体角色(鸭子)时,其他角色(玩家敌人)不变
"""


# 需求：以面向对象思想,描述下列情景.
#     玩家攻击敌人,敌人受伤
#     (根据玩家攻击力，减少敌人的血量).
#     敌人还可以攻击玩家,玩家受伤
#     (根据敌人攻击力，减少血量,闪现红屏).

#

class Character:
    def __init__(self, hp=0, atk=0):
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        print("攻击")
        # 1. 编码时调用父
        #    运行时执行子
        target.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        print("呃~血量还剩", self.hp)
#-------------------------------------------------------

class Player(Character):
    # 彰显个性
    # 2. 子重写
    def damage(self, value):
        super().damage(value)
        print("闪现红屏")


class Enemy(Character):
    def damage(self, value):
        super().damage(value)
        print("头顶爆字")


player = Player(500, 50)
enemy = Enemy(100, 30)
# 3. 创建子
player.attack(enemy)
enemy.attack(player)
