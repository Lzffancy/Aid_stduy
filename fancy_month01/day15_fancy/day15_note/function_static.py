from common.iterable_tool import Iterable_tool

list01 = [2,5,4,5,6,78,8,7,89,9,7,8]

def condition03(number):
    return number % 3
def condition05(number):
    return number % 5




d03 = Iterable_tool.find_all(list01,condition03)  #condition03函数作为参数　传递给ｆｕｎc　让　findall 去调用condition03（）　　　　（回调
for each in d03:
    print(d03)


d05 = Iterable_tool.find_all(list01,condition05)
for each in d05:
    print(each)