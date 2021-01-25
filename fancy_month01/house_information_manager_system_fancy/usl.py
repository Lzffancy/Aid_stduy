"""
    用户界面层
    user show layer
"""
from bll import HouseManagerController


def __show_find_maxtotalprice_house():
    pass


class HouseInformationView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("1.显示所有房源信息\n"
              "2.显示最大XX信息，可选'1.area','2.total_price','3.unit_price'\n"
              "3.显示最小XX信息，可选'1.area','2.total_price','3.unit_price'\n"
              "4.总价升序\n"
              "5.面积降序\n"
              "6.查看所有‘二室一厅\n"
              "7.查看所有房型\n")
    def __user_select(self):
        user_chose =input("请输入项目数字：")
        if user_chose=='1':
            self.__show_all()
        elif user_chose == '2':
             user_input = input('请选择查找条件')
             self.__show_find_someting_max(user_input)
        elif user_chose == '3':
            user_input = input('请选择查找条件')
            self.__show_find_someting_min(user_input)
        elif user_chose == '4':
            self.__show_sortup_by_totalprice()
        elif user_chose == '5':
            self.__show_sortdown_by_totalprice()
        elif user_chose == '6':
            self.__show_find_all_2room1hall()
        elif user_chose == '7':
            self.__show_get_house_type()

    def __show_all(self):
        for each_house in self.__controller.list_houses:
            print(each_house.__dict__)

#---------------------------------------------------------------------
    def __show_find_someting_max(self,condition):
        print(self.__controller.find_someting_max(condition).__dict__)
    def __show_find_someting_min(self, condition):
        print(self.__controller.find_someting_min(condition).__dict__)
#----------------------------------------------------------------------
    def __show_sortup_by_totalprice(self):
         temp = self.__controller.sortup_by_totalprice()
         for item in temp:
             print(item.__dict__)
    def __show_sortdown_by_totalprice(self):
        temp = self.__controller.sortdown_by_totalprice()
        for item in temp:
            print(item.__dict__)
    def __show_find_all_2room1hall(self):
        temp = self.__controller.find_all_2room1hall()
        for item in temp:
            print(item.__dict__)
    def __show_get_house_type(self):
        temp = self.__controller.get_house_type()
        for item in temp:
            print(item,temp[item],'个房源')
    # def to_show(self,object):
    #     print(object.__dict__)




    def main(self):
        while 1:
            self.__display_menu()
            self.__user_select()

if __name__ == '__main__':
   v01 = HouseInformationView()
   #v01.__user_select()        #因为设置了私用方法所有是无法通过　对象．ｆｕｎｃ()去调用的　
   #v01.show_all()
   v01.main()

