#class Commdity:　cid name price
class CommdityModel:
    def __init__(self, name='', price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid
    def __str__(self):
        return str(self.__dict__)
#------------------------------------------------------------------------
class CommdityView:
    def __init__(self):
        self.__controller = CommdityController() #v调用ｃ　　内构
#-------------------------
    def __display_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")
    def __select_menu(self):
        select = input("输入选项：")
        if select == "1":
            self.__input_commdityinfo()
        elif select == "2":
            self.__show_commdityinfo()
        elif select == "3":
            self.__delete_commdityinfo()
        elif select == "4":
            self.__modify_commdityinfdo()
        elif select == "5":
            pass

    def __input_commdityinfo(self):
        commdityinfo = CommdityModel()   #创建对象　Ｖ调用m

        commdityinfo.name = input("商品名称")
        commdityinfo.price =input("商品价格")
        #commdityinfo.cid = int(input("商品ｉｄ码"))
        self.__controller.add_commdity(commdityinfo)
        print("添加成功")

    def __show_commdityinfo(self):
        for each in self.__controller.list_commditise:
            print(each)

    def __delete_commdityinfo(self):
        cid = int(input("输入需要删除的商品ｃｉｄ:"))
        if self.__controller.remove_commdity(cid):
            print("删除成功")
        else:
            print("未找到，或删除失败")

    def __modify_commdityinfdo(self):
        commdityinfo = CommdityModel()
        commdityinfo.cid = int(input("需要修改的商品的cid"))
        commdityinfo.name = input("新商品名称")
        commdityinfo.price = input("新商品价格")
        if self.__controller.upadte_commdityinfo(commdityinfo):
            return print("修改成功")
        else:
            return print("修改失败，或未找到数据")

# ------------------------
    def main(self):
      while 1:
        self.__display_menu()
        self.__select_menu()

#------------------------------------------------------------------------
class CommdityController:
    def __init__(self):
      self.__list_commdity = []
      self.__cid = 1000

    @property                    #使得私有地址可读
    def list_commditise(self):
        return self.__list_commdity

    def add_commdity(self, target):
         target.cid = self.__cid
         self.__list_commdity.append(target)
         self.__cid += 1

    def remove_commdity(self, cid):
        for i in range(len(self.__list_commdity)):
            if self.__list_commdity[i].cid == cid:  #根据列表的.cid
                print('删除...',self.__list_commdity[i])
                del self.__list_commdity[i]
                return True
        return False

    def upadte_commdityinfo(self, commdityinfo):
        for each in self.__list_commdity:
            if each.cid == commdityinfo.cid:
                each.__dict__ = commdityinfo.__dict__
                return True
        return False

#---------------------------
managerview = CommdityView()
managerview.main()