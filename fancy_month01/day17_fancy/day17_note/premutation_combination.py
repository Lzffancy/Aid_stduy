'排列组合'
#排列
['男１','男2','男3']
['女１','女2','女3','女4']
import itertools
list_person = ['女１','女2','女3','女4','男１','男2','男3']
for item in itertools.permutations(list_person,3):
    print(item)

# 练习1:得知某个人的密码可能使用的字符有:
#   ABCDEFG012345
#  请计算6位密码的所有可能性
list_key = 'ABCDEFG012345'
for item in itertools.permutations(list_key,6):
    print(item)

# list_number1 =[1,2,3,4,5]
# list_number5 =[0,2,4]
# list_number2_4 =[0,1,2,3,4,5]
# count02 = 0
# for item in itertools.permutations(list_number2_4,3):
#     print(item)
#     count02 += 1
# print('有%d种2-4' ,count02)
# print(count02)

#-----------------------------------
# 练习2:"012345"字符可以组成多少个不重复的5位偶数
count012345 =0
str_number = "012345"
for item in filter(lambda item: item[0] != "0" and int(item[-1]) % 2 == 0, itertools.permutations(str_number, 5)):
    count012345 += 1
print(count012345)
#_---------------------------------
#组合
count_poker = 0
list_poker = ["红桃３","大王",'梅花５','黑桃Ａ']
for item in itertools.combinations(list_poker,2):
    print(item)
    count_poker += 1
print(count_poker)