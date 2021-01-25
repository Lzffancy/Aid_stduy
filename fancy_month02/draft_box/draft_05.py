# with open('1.txt','wb',buffering=1) as f:
#     while 1:
#      data = input('>>')
#      print(data.encode())
#      f.write(data.encode())
#      f.flush()
#
#
#
#



#  while 1:
#  data = input('>>')
#  print(data.encode())
import re
s8 = '192.168.1.6'
print(re.search(r"(\d{1,3}\.){3}\d{1,3}", s8).group())

s7 = '2,234,567'
print(re.search(r"\d{1,3}(,\d{1,3}){2}", s7).group())

s7 = '2,234,567'
print(re.findall(r"\d{1,3}(,\d{1,3}){1}", s7))

import re
s = 'abcd'
exp = (r'(\w)+', r'(\w)?', r'(\w)*')
for e in exp:
    print('\n表达式:', e)
    for i, m in enumerate(re.finditer(e, s)):
        print('第%d次搜索' % (i + 1), m.group(), m.groups(), sep='\n')


print(re.search(r'(ab)+', 'ababababababababababababa').group())

