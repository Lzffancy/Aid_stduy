log_path = '/home/tarena/桌面/fancy_month02/day03_fancy/data_teacherdoc/info/inet.log'

def info(path):
    with open(path) as f:

        while 1:
         data = ''             #按行写入，写入一段,出一段，清空一次
         for line in f:
            if line == "\n":  # 整行只有换行符 作为切分
                break
            data += line
            #print(data)


         if data:
          print(data,end='')
          print('=============================================')
          yield data
         else:
          return None
if __name__ == '__main__':
   for i in info(log_path):
       pass

