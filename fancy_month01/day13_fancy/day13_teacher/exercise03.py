# 练习2：定义函数,根据生日(年月日),计算活了多天.
# 输入：2010   1   1
# 输出：从2010年1月1日到现在总共活了3910天
# 思路:  时间元组 --> 时间戳
#       当前时间戳 - 生日时间戳
#       秒数 --> 天
#       天 -24-> 小时 -60-> 分钟 -60--> 秒
import time


def get_life_day(year, month, day):
    str_time = "%d/%d/%d" % (year, month, day)
    tuple_time = time.strptime(str_time, "%Y/%m/%d")
    life_second = time.time() - time.mktime(tuple_time)
    return life_second / 60 / 60 / 24


print("%d" % get_life_day(1990, 12, 16))
