"""
    多继承
        同名方法解析顺序:继承列表顺序(广度有限)
        如果调用指定父类的同名方法:
            父类名.同名方法名(self)
"""


class A:
    def func01(self):
        print("A -- func01")


class B(A):
    def func01(self):
        print("B -- func01")
        super().func01()  # c


class C(A):
    def func01(self):
        print("C -- func01")
        super().func01()


class D(B, C):
    def func01(self):
        print("D -- func01")
        super().func01()
        # C.func01(self) # c


# D -> B -> C -> A
obj = D()
obj.func01()
