"""
100000以内质数之和
"""
from time import time

def timeis(func):
    def wrapper(*args,**kwargs):
        start_time = time()
        res = func(*args,**kwargs)
        end_time = time()
        print("执行时间:",end_time - start_time)
        return res
    return wrapper


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

@timeis
def main():
    prime = []  # 存放所有质数
    for i in range(100001):
        if is_prime(i):
            prime.append(i)
    return sum(prime)

# 执行时间: 13.267135858535767
result = main()
print(result)