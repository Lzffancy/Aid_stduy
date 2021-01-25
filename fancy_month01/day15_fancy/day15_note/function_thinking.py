list01 = [2,5,4,5,6,78,8,7,89,9,7,8]

def condition03(number):
    return number % 3
def condition05(number):
    return number % 5



def find_all(func):  #使用参数func隔离　　不变ｆｉｎｄ_all　（处理逻辑）　和可变的ｃｏｎｄｉｔｉｏｎｘ（算法）
    for number in list01:
        if not func(number):
            #print(number._dict_)
            yield number

d03 = find_all(condition03)  #condition03函数作为参数　传递给ｆｕｎc　让　findall 去调用condition03（）　　　　（回调
for each in d03:
    print(d03)


d05 = find_all(condition05)
for each in d05:
    print(each)