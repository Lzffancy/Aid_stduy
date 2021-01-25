

class Wife:
    count = 0

    def __init__(self, name):
        self.name = name
        Wife.count += 1       #类名。访问类变量
    @classmethod
    def print_count(cls):
        print("有",cls.count,'个')




p2 = Wife('2')

p3 = Wife('3')

p4 = Wife('4')
print(p4.count)       #实例访问类变量
Wife.print_count()