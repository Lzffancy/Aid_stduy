"""
    Python 核心
    一.程序执行方式
        交互式:测试简单代码
            python3 -- 进入
            编码
            exit() -- 离开
        文件式:
            cd 根目录
            python3 文件名.py
    二.执行过程
        源代码-编译->字节码-解释->机器码
        只有导入的模块,才会生成字节码文件(pyc)
        编译目的:提高执行速度
        解释目的:跨平台
    三.Python内存管理机制
        1.引用计数：
            每个对象记录被变量绑定(引用)的数量,
            当为0时被销毁。
          缺点:循环引用 - 垃圾存储垃圾，占用内存。
        2.标记清除
            对内存空间全盘扫描,标记不再使用的数据.
            (不释放数据)
          缺点:速度慢
        3. 分代回收
            将内存空间划分为小中大三代.
            每次创建新数据时,在小代存储.
            当内存告急时,会触发标记清除,扫描当代内存空间.
            将有用的数据升代,释放旧数据内存空间.
        4. 内存优化
            尽少产生垃圾,对象池,配置垃圾回收器
    四.运算符
        身份运算符is: 判断两个变量存储的数据是否为同一个

    五.容器
        特点:
            字符串:存储字符编码,不可变,序列
            列表:存储变量,可变,序列
            元组:存储变量,不可变,序列
            字典:存储键值对,可变,散列
                键:唯一且不可变数据
            集合:存储键,可变,散列
        类型转换:
            列表 = list( 可迭代对象 )
            元组 = tuple( 可迭代对象 )
            # 格式:
            字典 = dict( 可迭代对象 )

    六.函数
        可变/不可变传参区别:
            可变:列表/字典/集合/自定义对象...
            不可变:字符串/数值/bool...
            区别:
                函数内部修改可变对象,无需通过return返回结果
                应用:列表排序函数,不用返回值
        参数
            实际参数
                位置实参:按顺序与形参进行对应
                    函数名(数据1,数据2)
                序列实参:拆
                    函数名(*序列)
                关键字实参:按名称与形参进行对应
                    函数名(形参名1 = 数据1,形参名2 = 数据2)
                字典实参:拆
                    函数名(**字典)

            形式参数
                默认形参:实参可选
                    def 函数名(形参名1 = 数值,形参名2= 数值)
                位置形参:实参必填
                    def 函数名(形参名1,形参名2)
                命名关键字形参:必须使用关键字实参
                    def 函数名(*,形参名1)
                    def 函数名(*args,形参名1)
                不定长参数:实参数量任意
                    def 函数名(*args)
                    def 函数名(**kwargs)
        递归
            思想:将大问题转移给范围缩小的子问题
            定义:函数内部调用自身的过程
            价值:以简单的方式,解决复杂问题.
            缺点:性能消耗大
"""

a = 10
b = a  # 10的引用计数为2
del a, b

c = 50
c = 60

list01 = []
list02 = []
list01.append(list02)
list02.append(list01)

# str_result = ""
# for number in range(10):
#     # str_result += str(number)
#     str_result = str_result + str(number)
# print(str_result)

# 频繁修改:用可变对象,代替不可变对象.
list_result = []
for number in range(10):
    list_result.append(str(number))
print(list_result)

# 对象池(内置对象池:字符串池.整数迟,小数池,bool池):
# 当数据创建时,会判断池中是否具有相同成员
# 如果没有,开辟空间创建新数据
# 如果有,直接返回数据地址,不再创建新数据.
# 优点:提高内存利用率
data01 = 10
data02 = 10
print(id(data01))
print(id(data02))

# True 表示是同一对象
# False 表示不是同一对象
print(data01 is data02)

list01 = [10]
list02 = list01
print(list01 is list02)  # True

# 列表元素必须能够一分为二
list01 = ["aA", ("b", "B"), ["c", "C"]]
dict01 = dict(list01)  # {'a': 'A', 'b': 'B', 'c': 'C'}
print(dict01)
# 列表存储的是key
list02 = list(dict01)
print(list02)  # ['a', 'b', 'c']
# 列表存储的是key和value
list02 = list(dict01.items())
print(list02)  # [('a', 'A'), ('b', 'B'), ('c', 'C')]

list03 = [1, 2, 3]
list04 = list(list03)  # list03[:]
list03[0] = 10
print(list04[0])  # 1


def func01(p1, p2):
    p1[0] = 10
    p2 = 10


list01 = [1]
list02 = [1]
func01(list01, list02)
print(list01)  # 10  函数内部,必须通过索引修改
print(list02)  # 1


# 需求:阶乘
# 3 * 2 * 1
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


print(factorial(3))
