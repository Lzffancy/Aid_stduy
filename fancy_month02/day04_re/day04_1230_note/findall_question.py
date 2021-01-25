import re
s8 = '192.168.1.6'
print(re.search(r"(\d{1,3}\.){3}\d{1,3}", s8).group())

s7 = '2,234,567'
print(re.search(r"\d{1,3}(,\d{1,3}){2}", s7).group())

s7 = '2,234,567'
print(re.findall(r"\d{1,3}(,\d{1,3}){2}", s7))

import re
s = 'abcd'
exp = (r'(\w)+', r'(\w)?', r'(\w)*')
for e in exp:
    print('\n表达式:', e)
    for i, m in enumerate(re.finditer(e, s)):
        print('第%d次搜索' % (i + 1), m.group(), m.groups(), sep='\n')
