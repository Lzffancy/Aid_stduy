'''
文件偏移量
'''

with open('2.txt','r+') as f:
    f.seek(-3,2)
    data = f.read()
    print(data)
#


