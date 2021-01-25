import time
def get_live_time(year='',moth='',day=''):
    str_time = "%s-%s-%s" % (year, moth, day)
    tuple_time = time.strptime(str_time, "%Y-%m-%d")

    tag_time_birthday = time.mktime(tuple_time)
    tag_time_now = time.time()
    tag_time_result = tag_time_now -tag_time_birthday
    print("出生日期",str_time)
    print(tag_time_result)

    live_day = tag_time_result/24/60/60
    return live_day






if __name__ == '__main__':
 print('%.2f'%get_live_time(year='1998',moth='10',day='4'))