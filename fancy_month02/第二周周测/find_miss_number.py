"""
找到缺失的数字

"""


class Find_miss_number_in():
    def __init__(self, number_list):
        self.number_list = number_list

    def process(self):
        set_miss = set(self.number_list)

        max_num = max(self.number_list)
        set_full = {num for num in range(max_num + 1)}
        # print(set_full)

        miss_num = set_full ^ set_miss
        return miss_num


if __name__ == '__main__':
    miss_num = Find_miss_number_in([0, 1, 2, 3, 4, 5, 6, 7, 9, 20,25])
    for num in miss_num.process():
        print(num,end=' ')
