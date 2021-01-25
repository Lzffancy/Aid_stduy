"""
    生成器表达式
        列表存储结果
            优点:获取数据灵活(索引切片,反复操作)
            缺点:内存占用较大

        生成器存储结果
            优点:节省内存
            缺点:获取数据不灵活(不能用索引切片,只能使用一次)
"""
# 列表推导式
# 将1-10之间数字的平方存入列表
list_result = [number ** 2 for number in range(1, 11)]
for item in list_result:
    print(item)

# 将1-100之间能被3整除的数字存入列表
list_result = [number for number in range(1, 101) if number % 3 == 0]
for item in list_result:
    print(item)

# 生成器表达式
generator_result = (number ** 2 for number in range(1, 11))
for item in generator_result:
    print(item)

for item in generator_result:
    print(item)

generator_result = (number for number in range(1, 101) if number % 3 == 0)
for item in generator_result:
    print(item)
