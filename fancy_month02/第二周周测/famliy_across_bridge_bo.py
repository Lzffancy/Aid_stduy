"""
小明过桥(算法优化）
"""

class FamilyBridge():
    def __init__(self):
        self.family_start = [1, 3, 6, 8, 12]
        self.family_end = []
        self.time_counter = 0
        self.step = []

    def start_two_to_end(self, person_list):
        self.family_start.remove(person_list[0])
        self.family_start.remove(person_list[1])

        self.family_end.extend(person_list)
        # 记录
        self.counter_step(person_list)

        # print(self.family_start)
        # print(self.time_counter)

    def end_one_to_start(self):
        one_person = [min(self.family_end)]
        self.family_end.remove(one_person[0])
        self.family_start.extend(one_person)

        # 记录
        self.counter_step(one_person)

    def counter_step(self, person_list):
        self.step.append(person_list)
        self.time_counter += max(person_list)

    def process(self):

        while 1:
            # start位最小两个过桥
            two_person = sorted(self.family_start)[:2]
            self.start_two_to_end(two_person)
            # end位最小的一个回去送手电-------------------
            self.end_one_to_start()
            # start位最大两个过桥----------------------------
            two_person = sorted(self.family_start)[-1:-3:-1]
            self.start_two_to_end(two_person)
            # 判断开始位置是否为空
            if not self.family_start:
                break
            # end位最小的一个回去送手电--------------------------
            self.end_one_to_start()

if __name__ == '__main__':
    across = FamilyBridge()
    across.process()
    print(across.step)
    print(across.time_counter)


