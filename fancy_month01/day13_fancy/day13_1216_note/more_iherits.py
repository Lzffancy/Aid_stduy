"""多继承
　　同名函数调用继承广度优先"""

class A:
    def func01(self):
        print("A")
        super().func01()


class B:
    def func01(self):
        print("B")


class C(A,B):
    def func01(self):
        print("C")
        super().func01()


class D(A, B):
    def func01(self):
        print("D")
        super().func01()
        #C.func01(self)   只调用Ａ

class E(C,D):
    def func01(self):
        print("E")
        super().func01()
if __name__ == '__main__':
    e = E()
    e.func01()