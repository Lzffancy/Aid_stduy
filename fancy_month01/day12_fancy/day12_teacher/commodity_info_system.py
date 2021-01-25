class CommodityModel:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.__dict__)


class CommodityView:
    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commoditys()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        commodity.price = int(input("请输入商品单价:"))
        self.__controller.add_commodity(commodity)
        print("添加成功")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_commoditys(self):
        for item in self.__controller.list_commoditys:
            print(item)

    def __delete_commoditys(self):
        cid = int(input("请输入商品编号:"))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")


class CommodityController:
    def __init__(self):
        self.__list_commoditys = []
        self.__start_id = 1001

    @property
    def list_commoditys(self):
        return self.__list_commoditys

    def add_commodity(self, target):
        target.cid = self.__start_id
        self.__start_id += 1
        self.__list_commoditys.append(target)

    def remove_commodity(self, cid):
        for i in range(len(self.__list_commoditys)):
            if self.__list_commoditys[i].cid == cid:
                del self.__list_commoditys[i]
                return True
        return False


view = CommodityView()
view.main()
