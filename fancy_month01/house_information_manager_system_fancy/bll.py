"""
    业务逻辑层
""" 
from dal import HouseDao
class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()
    @property
    def list_houses(self):
        return self.__list_houses
#---------------此处可以优化---------------------------------------------
    def find_someting_max(self,condition):
       if condition=='1':
        return max(self.list_houses,key= lambda item:item.area)
       elif condition=='2':
        return max(self.list_houses,key= lambda item:item.total_price)
       elif condition=='3':
        return max(self.list_houses,key= lambda item:item.unit_price)
    def find_someting_min(self, condition):
       if condition == '1':
           return min(self.list_houses, key=lambda item: item.area)
       elif condition == '2':
           return min(self.list_houses, key=lambda item: item.total_price)
       elif condition == '3':
           return min(self.list_houses, key=lambda item: item.unit_price)

       #b = iter_helper.get_max(self.list_houses,lambda item:item.total_price)
#--------------------------------------------------------------
    def sortup_by_totalprice(self):
        return sorted(self.list_houses,key=lambda item:item.total_price)
    def sortdown_by_totalprice(self):
        return sorted(self.list_houses, key=lambda item: item.area,reverse=True)
#--------------------------------------------------------------
    def find_all_2room1hall(self):
     list_2room1hall=[]
     for i in range(len(self.__list_houses)-1):
        if self.__list_houses[i].house_type =='2室1厅':
            list_2room1hall.append(self.__list_houses[i])
     return list_2room1hall
    #
    # def sort_by_housetype(self):
    #     housetype =[]
    #     countlist ={}
    #     for i in range(len(self.__list_houses) - 1):
    #         if self.__list_houses[i].house_type not in housetype:
    #             housetype.append(self.__list_houses[i].house_type)
    #         else:

    def get_house_type(self):
        dict_result = {}
        for house in self.__list_houses:
            # 如果存在该房源类型，计数增加
            if house.house_type in dict_result:
                dict_result[house.house_type] += 1
            else:
                dict_result[house.house_type] = 1
        return dict_result


if __name__ == '__main__':
   c01 = HouseManagerController()
   temp = c01.find_all_2room1hall()
   for each in temp:
       print(each.__dict__)