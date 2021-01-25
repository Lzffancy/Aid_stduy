"""
    使用闭包模拟以下情景：
        在银行开户存入10000
        购买xx商品花了xx元
        购买xx商品花了xx元

    要求:写完代码调试
        画出内存图
"""


# 有外有内:存钱/花钱
# 内使用外:修改存款
# 外返回内:返回购买行为

def create_account(money):
    print(f"在银行开户存入{money}")

    def buy(commodity, price):
        nonlocal money
        money -= price
        print(f"购买{commodity}商品花了{price}元")

    return buy


# 调用外函数,得到内函数
action = create_account(10000)
# 调用内函数
action("手机", 5000)
action("游戏机", 2000)
action("游戏卡", 3000)
