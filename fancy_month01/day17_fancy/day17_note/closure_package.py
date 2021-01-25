'''
    闭包
    逻辑连续
  闭包
    三大要素:
        有外有内
        内使用外
        外返回内
    字面思想:
        封闭内存空间
    作用:
        外部函数栈帧执行后,不释放.
        等待内部函数重复使用
'''
def give_gift_money(money):  #这就会开辟ｍｏney　栈帧　就有了ｍｏney变量
    print(f'获得',money)
    def buy_something(commdity,price):
        nonlocal money
        money -= price
        print('买了',commdity,'剩下',money)
    return buy_something



give_gift_money(1000)('口红',100)


#---------------------------------------
def bank_account(money):
    print("存入",money)
    def buy_something(commdity,price):
        nonlocal money          #nonlocal 声明需要调用闭包内　变量
        money -= price
        print('买了', commdity, '用了', price,'剩下', money)

    return buy_something


action = bank_account(10000)
action('英伟达３０８０t',4999)
action('英伟达３０８０t',4999)
