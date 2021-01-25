#想通过导入模块来处理异常，未成功
#
'''
def get_int(input_x,message):
    while 1:
      try:
          data = int(input(message)#此处出错会向上
          return data  #return 会终止函数
      except Exception:
         print("输入格式有误，请输入整数")

'''

#score = get_score()
#print("成绩是：%d"% score)
