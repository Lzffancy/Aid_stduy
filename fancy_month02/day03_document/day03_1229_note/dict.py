dict_path = '../data_teacherdoc/info/dict.txt'


def find_word(word):
    # word_lenth=len(word)
    # print(word_lenth)
    with open(dict_path, 'r') as f_dict:
        for line in f_dict:
            # print(line)
            if line.split(' ')[0] == word:
                print(line)
                return line
            elif line.split(' ')[0] >= word:  # 提升效率
                break
        print("查无此词")
        return None


if __name__ == '__main__':
    find_word('a')
