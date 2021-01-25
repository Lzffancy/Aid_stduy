"""
刷新缓冲
f.flush()　手动刷新
buffering=1　换行刷新
buffering=10　按照bytes刷新,写入二进制

"""
'''
with open('1.txt','ab') as f:
    while 1:
        data = input('>>')
        if not data:
            break
        f.write(data.encode())
        f.flush()
'''
import time

with open('1.txt', 'a+', buffering=1) as f:
    count = 1
    f.seek(0,0)
    count =len(f.readlines())
    while 1:
        count += 1
        get_time = time.ctime()
        f.write(str(count)+ '.' + get_time+ '我爱你' + '\n')
        #f.seek()
        time.sleep(2)
