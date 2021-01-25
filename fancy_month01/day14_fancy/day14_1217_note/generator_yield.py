'''练习1：定义函数,在列表中找出所有偶数
[43,43,54,56,76,87,98]'''

def get_number(list01):
    for num in list01:
        if num % 2 == 0:
          yield num

num2 = get_number([43,43,54,56,76,87,98])
for each in num2:
    print(each)

'''练习2. 定义函数,在列表中找出所有数字
 [43,"悟空",True,56,"八戒",87.5,98]'''
def get_number02(list01):
    for item in list01:
        if type(item) == float or type(item)==int:
            yield item

for each in get_number02([43,"悟空",True,56,"八戒",87.5,98]):
    print(each)
    # 1. 将yield关键字以前的代码存入__next__函数体
    # 2. 将yield关键字以后的数据作为__next__函数返回值