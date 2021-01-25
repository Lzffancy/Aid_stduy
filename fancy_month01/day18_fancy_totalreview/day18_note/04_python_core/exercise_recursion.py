'''
  递归
            思想:将大问题转移给范围缩小的子问题
            定义:函数内部调用自身的过程
            价值:以简单的方式,解决复杂问题.
            缺点:性能消耗大
'''
def recursion_ex(n):
    if n <= 1:
        return 1
    # print(n)
    return n * (-1) ** (n + 1) + recursion_ex(n - 1)


print(recursion_ex(3), 'result')


# -----------------------------------------

def recrusion_list(list_n):
    for item in list_n:
        if type(item) != int:
            recrusion_list(item)
        else:
            print(item)


list01 = [1, 2, [3, [4, 5], 6], 7, [8, 9]]

recrusion_list(list01)
