import time
print(time.localtime())
tuple_time = time.localtime()
print(tuple_time[3:6])

print(time.time())
time_tag = time.time()

print(time.mktime(tuple_time),"元组——>戳")
print(time.localtime(time_tag),"戳——>元组")

print(time.strftime('%Y %m %d %h %m %S',tuple_time))
print(time.strptime("2020/12/16 14:46:40", "%Y/%m/%d %H:%M:%S"))