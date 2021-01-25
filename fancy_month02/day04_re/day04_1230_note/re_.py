import re

# 匹配单个－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
s = "www.baidu.com/www.toomc.cn"
print(re.findall('com|cn', s))  # 满足一个条件即可

s2 = 'abcdef'
print(re.findall('ab|bc|cd', s2))  # 短路

print(re.findall('张.丰', "张三丰,张四丰,张五丰"))  # 任意单个
print(re.findall('张...', "张三丰,张四丰,张五丰"))

print(re.findall('[aeiou]', "How are you!"))  # 字符集，一次匹配单个　　
print(re.findall('[a-c]', "How are you!"))
print(re.findall('[!a-c]', "How are youasdkjasiododd!ps!dchphsdfhphvp!"))

print(re.findall('[^0-9A-Za-z]', "Use 007 port"))  # 除了

# 匹配重复-----------------------------------------------------------
print(re.findall('wo*', "wooooo~~w!"))  # 0或多
print(re.findall('[wo]*o', "wooooo~~wooo--wowo!"))

print(re.findall('[A-Z][a-z]+', "Hello World"))  # 至少一次

print(re.findall('-?[0-9]+', "Jame,age:18, -26,---1A55"))  # ? n0或１

print(re.findall('1[0-9]{10}', "Jame:13886495728"))  # 限定出现次数
print(re.findall('wo{3}', "wooooo~~wooo--wowo!"))

print(re.findall('[1-9][0-9]{5,10}', "Baron:1259296994"))  # 出现５－１０次
print(re.findall('wo{1,2}', "wooooo~~wooo--wowo!"))

# 位置匹配----------------------------------------------------------------
print(re.findall('^How', "How are youhsdfhphvp!How"))  # 以开始
print(re.findall('How$', "How are youachphhphvpHow"))  # 以结尾
print(re.findall('^How$', "How"))  # 绝对匹配
print(re.findall(r'\bis\b', "This is a test."))

# 字符相关匹配------------------------------------------------------------
print(re.findall('\d{1,4}', "Mysql3306http:80"), 'FLAG')
print(re.findall('\D+', "Mysql: 3306, http:80"))

print(re.findall('\w+', "server_port = 8888"))
print(re.findall('\w', "server_port = 8888"))
print(re.findall('\W', "server_port = 8888"))

print(re.findall('\w+\s+\w+', "hello    world"))
print(re.findall('\S+', "hello    world"))

# 贪婪-----------------------------------------
'''
特殊字符: . * + ? ^ $ [] () {} | \
重复匹配元字符后加？进入非贪婪模式
'''
print(re.findall(r'ad{3,5}?', 'aaaaaaaaddddddddddd'))
print(re.findall(r'ad*?c', 'adddccc'))

# 《奥特曼－迪迦》《奥特曼！迪迦》《奥特曼＠迪迦》
s6 = '《奥特曼－迪迦》《奥特曼！迪迦》《奥特曼＠迪迦》'
print(re.findall('《.+?》', s6))
# ()子组-------------------------------------------------------------
s7 = '张三1998 李四1447 王五1545'
print(re.findall('李四(\d{4})', s7))
# 表示优先级
print(re.search(r'(王|李)\w{1,3}', "王者荣耀　李卓凡").group())

# 捕获组－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
print(re.search(r'(?P<pig>ab)+', "ababababab").group())
print(re.search(r'(?P<pig>ab)+', "ababababab").group('pig'))
