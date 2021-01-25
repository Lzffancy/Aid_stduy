#

def get_score():
    while 1:
      try:
        input_score = int(input('输入学生成绩：'))  #此处出错会向上
        return input_score  #return 会终止函数
      except Exception:
         print("输入格式有误，请输入整数")



score = get_score()
print("成绩是：%d"% score)