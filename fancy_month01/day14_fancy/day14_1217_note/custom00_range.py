#
"""
    遍历自定义对象
"""

class Graphic_iterator:
    def __init__(self,data):   #这个ｄａｔａ 用来传递　self.__number　这个参数
        self.__i = 0
        self._data = data
    def __next__(self):             #next 在 iter　后调用
            if self.__i < self._data:
                result  = self.__i
                self.__i += 1
                return result
            else:
                raise StopIteration
class GraphicController:
    def __init__(self,number):
        self.__number = number
    def __iter__(self):
      return Graphic_iterator(self.__number)



for each in GraphicController(91111111):
    print(each)



'''
    iterator = controller.__iter__()
    while True:
        try:
            item = iterator.__next__()
            print(item)
        except StopIteration:
            break
'''