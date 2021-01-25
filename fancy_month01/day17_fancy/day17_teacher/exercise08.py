"""
    为原函数增加新功能(打印函数执行时间)
    执行时间 = 执行后　- 执行前
"""
import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        re = func(*args, **kwargs)
        stop_time = time.time()
        print("执行时间是：", stop_time - start_time)
        return re

    return wrapper


@print_execute_time
def sum_number(n):
    sum_value = 0
    for i in range(n):
        sum_value += i
    return sum_value


print(sum_number(10))
print(sum_number(1000000))
