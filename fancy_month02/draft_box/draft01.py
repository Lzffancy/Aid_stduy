class MyClass:
    def __init__(self, data="1000"):
        self.__data = data
        self.__listdata = []

    @property
    def data(self):
        print(self.__data,'私有值')
        return self.__data
    # @data.setter
    # def data(self, value):
    #     self.__data = value

    @property
    def listdata(self):
        print(self.__listdata,'私有值')
        return self.__listdata

    def modifi_listdata(self,data):
        self.__listdata=[data]

    def modifi_data(self,data):
        self.__data=data
m01 = MyClass()
# print(m01.data,'读取')
# print(m01.listdata,'读取')
#-------------------------------
m01.__data = 5000 #无法修改私有变量
#print(m01.data)
#m01.data = 5000
MyClass.data = 80
print(m01.data)

m01.modifi_data(50)
print(m01.data)

#------------------------------------
m01.listdata.append('lzf')
print(m01.listdata,'读取')
#----------------------------------可以修改私有列表
#m01.__listdata = 1
print(m01.listdata,'读取')
#----------------------------------不可以
m01.modifi_listdata(10)
print(m01.listdata,'读取')
#---------------------------------类内函数修改自己的私有
# class XXController:
#     def func01(self):
#         print("func01执行了")
#
#
# class XXView:
#     def __init__(self):
#         self.__controller = XXController()
#
#     def func02(self):
#         print("func02执行了")
#         self.__controller.func01()

#
# view = XXView()
# view.func02()