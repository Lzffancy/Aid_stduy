"""
小明过桥

"""
import random


def familyBridge():
    family_start = [1, 3, 6, 8, 12]
    family_end = []
    time_counter = 0
    step = []
    record_first_two = []

    while 1:
        # 第一次派最快的两人过桥
        #if not family_end:
            #two_person = sorted(family_start)[:2]
            #print(two_person)
        #else:
            # 选两人过桥，终点加两人，起点减少两人
        two_person = random.sample(family_start, 2)  # [  ]

        family_end.extend(two_person)

        family_start.remove(two_person[0])
        family_start.remove(two_person[1])
        # print(family_start)

        # 记录以上步骤
        step.append(two_person)  # 选择过桥的人
        # step.append(max(two_person))  # 过桥所用时间
        # print(step)
        time_counter += max(two_person)

        if not family_start:
            return time_counter, step

        # 再选终点 用时最少一人送手电到起点--------------------
        one_person = random.sample(family_end, 1)
        #one_person = [min(family_end)]
        family_start.extend(one_person)
        family_end.remove(one_person[0])

        # 记录以上步骤用时
        step.append(one_person[0])
        step.append("//")
        print(step)
        time_counter += one_person[0]


if __name__ == '__main__':
    try_counter = 0

    while 1:
        try_counter += 1
        time, step = familyBridge()
        if time < 30:
            print('最短用时%ss,随机尝试次数%s次，步骤%s' % (time, try_counter, step))
            break





#思路
'''import random

while True:
    # a岸
    a = [1, 3, 6, 8, 12]
    # b岸
    b = []
    # 速度
    SPEED = 0
    # 流程
    step = []

    while True:
        # 随机获取两个a中的元素
        x = random.sample(a, 2)
        # 将元素放入b中
        b.extend(x)
        # 从a中删除元素
        a.remove(x[0])
        a.remove(x[1])
        step.append(x)  # 将随机组合添加到列表
        step.append(max(x))  # 将随机组合的过河时间也添加到列表
        if not a:
            break

        # 从b中随机找一个到a
        y = random.sample(b, 1)
        a.extend(y)
        b.remove(y[0])
        step.append(y[0])  # 记录 返回的时间
        step.append('||')

    # print(step)
    for i in step:
        if type(i) == int:
            SPEED += i
    if SPEED <= 30:
        break
print(step)'''