# 练习1:得知某个人的密码可能使用的字符有:
#   ABCDEFG012345
#  请计算6位密码的所有可能性
import itertools

words = "ABCDEFG012345"
for item in itertools.permutations(words, 6):
    print(item)

# 练习2:"012345"字符可以组成多少个不重复的5位偶数
str_number = "012345"
for item in filter(lambda item: item[0] != "0" and int(item[-1]) % 2 == 0, itertools.permutations(str_number, 5)):
    print(item)
