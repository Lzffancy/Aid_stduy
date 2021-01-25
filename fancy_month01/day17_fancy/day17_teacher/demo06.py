"""
    闭包应用
        逻辑连续
            从得1000元,到不断购买商品的过程,不中断.
"""
# 压岁钱
def give_gife_money(money):  # 得钱
    print(f"获得{money}压岁钱")

    def child_buy(commodity, price):  # 花钱
        nonlocal money
        money -= price  # 压岁钱减少
        print(f"孩子花了{price}购买了{commodity},还剩下{money}")

    return child_buy  # 返回购买行为

aciton = give_gife_money(1000)
aciton("变形金刚", 200)
aciton("糖葫芦", 100)
aciton("彩票", 200)
