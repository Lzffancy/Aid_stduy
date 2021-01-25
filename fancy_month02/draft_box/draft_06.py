def func(*args):
    # print(args)
    # print(kwargs)
    for each in args:
        print(each,'1')

    # for each01 in kwargs:
    #     print(each01,'2')

#
# a =(1,2,3,)
# func(a)
#
# b = [4,5,6]
# func(b)

c ={'a':1,'b':2}
d = {'c':1,'d':2}
func(c,d)

