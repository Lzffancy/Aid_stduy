class MyClass:
    def __init__(self, data="1000"):
        self.__data = data
        print(self.data)
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

    def modifi_listdata(self,value):
        self.__listdata=[value]

    def modifi_data(self,value):
        self.__data=value
m01 = MyClass()
#-------------------------------
print(m01.data)
m01.__data = 5000  #外部不可以去直接赋值　　改变私有值
print(m01.data)
m01.modifi_data(1)  #通过实例方法去　修改私有
print(m01.data)


#=============================对列表设置为只读　也相当于改列表提供了修改方法
print(m01.listdata)
#m01.listdata = [7] #外部不可以去直接直接赋值　　设置私有列表
print(m01.listdata)
m01.modifi_listdata('7')
print(m01.listdata)    #通过实例方法去　修改私有
m01.listdata.append('8')
print(m01.listdata)