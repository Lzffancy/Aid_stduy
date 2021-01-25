#--------------------
list1 = [1,2,3]
for each in list1:
    print(each)

#--------------------

dict1 = {1:11,2:22,3:33}
iterator_dict1 = dict1.__iter__() #使其生成迭代器,dict成为迭代对象

while 1:
    try:
        key = iterator_dict1.__next__()    #使用迭代器　迭代出结果
        value =dict1[key]
        print(key,value)
    except StopIteration:
        break