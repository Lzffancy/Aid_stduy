# pic_path ='/home/tarena/桌面/share/pic.jpeg'
#
# with  open(pic_path,'rb') as pic_file:
#       pic = pic_file.read()
#       print(pic)

def find_how_to_anwser(recive_data):
      #recive_data = '你几岁啦'

      key_anwser = {'岁':"我三岁了!",
                    '是':'我是人工智障',
                    '?':'你凭什么给我发问号?',
                    "好":"我不好",
                    '哈':"闭嘴!!不许笑",
                    "名":'我叫AI,Fancy'}
      for item in key_anwser :
          for str_item in recive_data:
              if item == str_item:
                  return key_anwser[item]
      else:
          return "人家还小，不知道。"







if __name__ == '__main__':
   while 1:
       question = input(">>")
       find_how_to_anwser(question)