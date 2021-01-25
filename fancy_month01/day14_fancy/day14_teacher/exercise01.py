"""
    练习：创建函数，在终端中录入int类型成绩。如果格式不正确，重新输入。
    效果： score  = get_score()
           print("成绩是：%d"%score)
"""


# 有错误重新输入,直到正确返回整数
def get_score():
    while True:
        try:
            score = int(input("请输入成绩:"))
            return score  # 退出函数
        except:
            print("输入不是整数")


score = get_score()
print("成绩是：%s" % score)
