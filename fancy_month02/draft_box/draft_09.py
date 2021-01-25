# while 1 :
#     data =input('>>')
#     if not data:
#         print("结束")
# import os
# FTP_source = r'I:\AID2011\fancy_month02\day15_multi_concurrent\day15_0117_note\ftp_app\FTPsoure\/'
# filelist = os.listdir(FTP_source)
# print(filelist)

import hashlib
# print(hashlib.__doc__)
hash = hashlib.sha256()
hash.update(b"abc123")
print(hash.hexdigest())