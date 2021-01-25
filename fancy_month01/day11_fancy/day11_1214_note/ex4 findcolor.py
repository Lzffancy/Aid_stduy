class Color:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self, other):
        return (self.r + self.g +self.b) == (other.r +other.g +other.b)
        #self.__dict__ == other.__dict__
    def __gt__(self, other):
        return(self.r + self.g +self.b) > (other.r +other.g +other.b)

list_color =[
   Color(0,255,255),
   Color(1,105,100),
   Color(1,105,180)
]

c1 = Color(0,255,255)
c2 = Color(1, 105, 100)

print(c1>c2)
print(max(list_color).__dict__)

index01 = list_color.index(Color(1,105,100))
print(index01)