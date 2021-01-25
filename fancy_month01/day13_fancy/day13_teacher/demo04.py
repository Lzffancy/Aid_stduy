"""
    标准库模块 - 时间 time
"""

import time

# 人类时间: -221     公园元年  2020年12月16日
# 时间元组(年,月,日,时,分,秒,星期,年的第几天,与夏令时偏移量)
tuple_time = time.localtime()
# 获取月份
print(tuple_time[1])
# 获取时分秒
print(tuple_time[3:6])

# 机器时间:从1970年元旦开始  到 现在经过的秒
# 时间戳
print(time.time())  # 1608100385.2850263

# 时间元组 --> 时间戳
# 语法: 时间戳 = time.mktime(时间元组)
print(time.mktime(tuple_time))

# 时间戳 --> 时间元组
# 语法: 时间元组 = time.localtime(时间戳)
print(time.localtime(-10000000000))

# 时间元组  --->  字符串
# 语法:字符串 = time.strftime(格式,时间元组)
# 20/12/16 14:46:40
print(time.strftime("%y/%m/%d %H:%M:%S", tuple_time))
# 2020/12/16 14:46:40
print(time.strftime("%Y/%m/%d %H:%M:%S", tuple_time))

# 字符串  --->  时间元组
# 语法:时间元组 = time.strptime(字符串,格式)
print(time.strptime("2020/12/16 14:46:40", "%Y/%m/%d %H:%M:%S"))
