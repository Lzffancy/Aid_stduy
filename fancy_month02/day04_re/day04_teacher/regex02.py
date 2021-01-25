"""
re 模块使用 2
"""
import re

string = "Alex:1996,Sunny:1998"

# 匹配开始位置
result = re.match("(\w+):(?P<year>\d+)",string)
print(result.group(2))

# 匹配第一处
result = re.search("\d+",string)
print(result.group())


# result = re.finditer("\w+",string)
#
# # 迭代取值 获取每处匹配内容的match对象
# for item in result:
#     print("匹配内容：",item.group())
#     print("所在位置：",item.span())
