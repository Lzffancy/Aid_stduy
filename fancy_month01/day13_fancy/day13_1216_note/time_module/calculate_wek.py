import time
def get_week_name(year='',moth='',day=''):
    str_time ="%s-%s-%s" % (year,moth,day)
    tuple_time =time.strptime(str_time,"%Y-%m-%d")
    week_index = tuple_time[-3]
    print(week_index)
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week[week_index]






if __name__ == '__main__':
 get_week_name(year='2020',moth='12',day='16')
 print(get_week_name(year='2020',moth='12',day='16'))