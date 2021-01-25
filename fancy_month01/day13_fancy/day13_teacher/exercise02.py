"""
    练习1：定义函数,根据年月日,计算星期。
    输入：2020   9   15
    输出：星期二
"""
import time


def get_week_name(year, month, day):
    # 年月日 --> 年月日字符串
    # str_time = f"{year}/{month}/{day}"
    str_time = "%d/%d/%d" % (year, month, day)
    # 年月日字符串 --> 时间元组
    tuple_time = time.strptime(str_time, "%Y/%m/%d")
    # 时间元组 --> 星期数
    week_index = tuple_time[-3]
    # 星期数 --> 星期名
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week[week_index]


print(get_week_name(2020, 12, 16))
