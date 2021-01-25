'''
字节串
1.所有的　字符串　都可以对应上相应的字节串

2.但字节串不一定对应字符串　，还可以对应其他
'''
# 编码
str01 = "我爱你"
bytes02 = b"i love you"
bytes01 = str01.encode(encoding="utf-8")

print(type(bytes01))
print(bytes01)
print(type(bytes02))
print(bytes02)

# 解码
print(bytes01.decode())

#----------------------------------------------
#file_object = open()