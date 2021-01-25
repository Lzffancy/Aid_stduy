# 全局变量
list_merge = [2, 2, 8, 2]
g = 0


# (1). 定义函数,将零元素移动到末尾zero_to_end()
#  备注：操作全局变量
#     [2,0,2,0]  -->  [2,2,0,0]
#     [2,0,0,2]  -->  [2,2,0,0]
#     [2,4,0,2]  -->  [2,4,2,0]

def zero_to_end():
    for i in range(len(list_merge) - 1, -1, -1):
        #print(i)
        if list_merge[i] == 0:# 读取全局　修改列表元素 不需要将列表声明为全局
            del list_merge[i]
            list_merge.append(0)

def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        #print(i)
        if list_merge[i] == list_merge[i+1]:# 读取全局　修改列表元素 不需要将列表声明为全局
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            #print(list_merge)
            list_merge.append(0)




if __name__ == '__main__':
    merge()
    print(list_merge)
