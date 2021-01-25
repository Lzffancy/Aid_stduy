'''
to find Hardware address
'''
import re
log_path ='/home/tarena/桌面/fancy_month02/day03_fancy/data_teacherdoc/info/inet.log'
def find_Hd_address(name='',path=''):


    with open(path) as f_log:
        f_log.seek(0, 0)
        readline_count = 0

        for line in f_log:
            readline_count += 1
            if line.split(' ')[0] ==name:
                print(line)
                hardware_line = readline_count
                print(hardware_line)

                #print(f_log.readlines()[hardware_line-2])
                address_text = f_log.readlines()[hardware_line-2]
                print(address_text)
                print(re.findall('([0-9a-f]{4}\.){2}[0-9a-f]{4}', address_text))
                f_log.seek(0, 0)
                break
        #print(f_log.tell())


#文件的偏移量存在问题，导致无法准确找到address所在行　（待解决






if __name__ == '__main__':
    find_Hd_address('BVI100',log_path)

