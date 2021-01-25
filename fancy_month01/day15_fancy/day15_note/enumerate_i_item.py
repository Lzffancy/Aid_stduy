# 可迭代对象具有——ｉｔｅｒ__，但
# 只有在执行迭代操作时候才生成一个迭代器，去找————ｎｅｘt——依次迭代
list01 = [0,1,2,2,3,4,5,6,3,3,5,4]
for i,item in enumerate(list01):
    pass

for item in list01:
    print(item)

enumerate(list01)    #建立一个生成器（枚举）


#--------------------------------------
'''练习1：将列表中所有奇数设置为None
   练习2：将列表中所有偶数自增1
'''
for i, item in enumerate(list01):
    if item % 3 == 0:
       list01[i] = None
    else:
       list01[i] += 1


print(list01)