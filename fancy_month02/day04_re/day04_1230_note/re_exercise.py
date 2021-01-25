import re

print(re.findall('[A-Z][a-z]*', ' A Hi,Jame. How are you!'))

s = '-12度气温，183的战士背着30kg的装备'
print(re.findall('-?[0-9]+', s))

s2 = '我的手机号码是15200536624,qq号码时731566721,13548185585'
print(re.findall('1[3578][0-9]{9}', s2))

s3 = '张三　54115484　李四115515151 lizf151111'
print(re.findall('[0-9]{6,11}', s3))

print(re.findall('^How', "How are youasdkjasiododd!ps!dchphsdfhphvp!How"))
print(re.findall('How$', "How are youasdkjasiododd!ps!dchphsdfhphvpHow"))
print(re.findall('^How$', "How"))

# -----------------------------------------------------------
s4 = '13 9 -4 3.14 -2.6 '
print(re.findall(r'-?\d+\.?\d*', s4))

# -------------------------------------------------------
s5 = '日薪　$150'
print(re.findall(r'\$\d+', s5))

'''特殊字符: . * + ? ^ $ [] () {} | \
   匹配元字符后加？进入非贪婪模式
'''

# ---------------------------------------
print(re.findall(r'ad{3,5}?', 'aaaaaaaaddddddddddd'))
print(re.findall(r'ad*?c', 'adddccc'))

print(re.findall(r'ad??', 'aaaaaaaaddddddddddd'))

# -----------------------------------------
# 《奥特曼－迪迦》《奥特曼！迪迦》《奥特曼＠迪迦》
s6 = '《奥特曼－迪迦》《奥特曼！迪迦》《奥特曼＠迪迦》'
print(re.findall('《.+?》', s6))
# 表示子组输出----------------------------------------
s7 = '张三1998 李四1447 王五1545'
print(re.findall('李四(\d{4})', s7))



# 表示优先级
print(re.search(r'(王|李)\w{1,3}', "王者荣耀　李卓凡").group())
print(re.search(r'(ab)+', 'ababababababababababababa').group())

# 捕获组－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
print(re.search(r'(?P<pig>ab)+', "ababababab").group())
print(re.search(r'(?P<pig>ab)+', "ababababab").group('pig'))

# -------------------------------------------------------------
s8 = '192.168.1.6'
print(re.search(r"(\d{1,3}\.){3}\d{1,3}", s8).group())

# --------------------------------------------------------------
s9 = '430406199810042554'
print(re.search(r'\d{6}\d{4}\d{2}\d{2}\d{3}\d{1}', s9).group())

# -------------------------------
'''
re的使用
'''
string = 'Alex:1989,Suuy:1998'
result = re.findall("\w+:\d+", string)
print(result)
# 返回列表　但内部是元组
result02 = re.findall("((\w+):(\d+))", string)
print(result02)
#re.split
result03 = re.split('\W+',string)
print(result03)
# re.sub
result04 =re.sub('\d','**',string,count=0)
print(result04)

#_____________________以下返回值为match.object__
#re.finditer
result05 = re.finditer('\w+',string)
for item in result05:
    print(item.group(),'9999')
    print(item.span())#切片数字

#re.match  开始位置符合^
result06 =re.match("\w+",string)
print(result06.group())

#re.serach 内容符合(第一处）
result07 = re.search('\w+',string)
print(result07.group())
