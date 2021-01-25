#
dict_path = '../data_teacherdoc/info/dict.txt'


def copy(filename):
    with open(filename, "rb") as f:
        with open(filename + '副本', 'wb') as f_copy:
            while 1:
                temp_data_byte = f.read(256)
                if  temp_data_byte :
                    f_copy.write(temp_data_byte)
                else:
                    print('复制完成')
                    break



if __name__ == '__main__':
    copy(dict_path)
