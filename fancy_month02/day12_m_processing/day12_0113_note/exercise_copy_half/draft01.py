"""
负责分割
负责读取拷贝
"""
import os
def copy_by_index(index_start,index_end,file_name,new_file):
    #f_size = os.path.getsize(file_name)

    with open(file_name,'rb') as f:
         data = f.read(index_end)
    with open(new_file,'wb') as f_new:
         f_new.write(data)


def split_half():
    f_size = os.path.getsize(file_name)  #字节数
    pass
