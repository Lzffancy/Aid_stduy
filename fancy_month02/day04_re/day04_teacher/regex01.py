"""
re 模块基本函数
"""
import re

string = "Alex:1996,Sunny:1998"

# 使用## 替换正则表达式匹配到的内容
result = re.sub("\W+","##",string,2)
print(result)

# 使用匹配内容分割字符串
# result = re.split("\W+",string)
# print(result)

# 如果正则表达式有子组，那么只返回子组对应内容
# result = re.findall("(\w+):(\d+)",string)
# print(result)