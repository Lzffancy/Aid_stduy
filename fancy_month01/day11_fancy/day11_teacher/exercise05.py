"""
    练习1：以面向对象思想，描述下列情景
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
"""


# 增加新攻击目标(鸭子),手雷类不变.
class Grenade:
    def explode(self, target):
        print("爆炸")
        # 先用
        # 1. 调用父
        target.damage()


class AttackTarget:
    def damage(self):
        pass


class Player(AttackTarget):
    # 2. 子重写
    def damage(self):
        print("碎屏")


class Enemy(AttackTarget):

    def damage(self):
        print("头顶爆字")


g01 = Grenade()
p01 = Player()
e01 = Enemy()
# 3. 创建子
g01.explode(p01)
g01.explode(e01)
