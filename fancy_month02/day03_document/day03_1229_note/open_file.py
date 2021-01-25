'''
打开文件
'''
# f = open("1.txt", 'r') #可迭代对象
# while 1:
#  content = f.read(2) #2的n次方倍　　此方式在读取大文件有优势
#  print(content,end="")
#  if content==None:
#      break


# for each in f:
#     print(each)


# f2 = open("2.txt",'w') #会先清空
# a+　的偏移量在结尾　
f3 = open('3.txt', 'r+')
content03 = f3.read()
#print(content03)



# 按行读取
# content_list = f3.readlines()
# print(content_list,'1')

#写入
n = f3.write("hhhh\n")#.encode())
print('当前写入字符数',n)
list01 = ['继续','不要停','继续敲','\n']
f3.writelines(list01)
print(content03)