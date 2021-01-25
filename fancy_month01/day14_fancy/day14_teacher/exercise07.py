# 练习1：定义函数,在列表中找出所有偶数
#   [43,43,54,56,76,87,98]
def get_evens(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item


for item in get_evens([43, 43, 54, 56, 76, 87, 98]):
    print(item)


# 练习2. 定义函数,在列表中找出所有数字
#  [43,"悟空",True,56,"八戒",87.5,98]
def get_numbers(list_target):
    for item in list_target:
        if type(item) in (int, float):
            yield item


for item in get_numbers([43, "悟空", True, 56, "八戒", 87.5, 98]):
    print(item)
