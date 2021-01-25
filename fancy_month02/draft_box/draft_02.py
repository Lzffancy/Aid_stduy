"""
小明过桥

"""

class FamilyBridge():
    def __init__(self):
        self.totall_time = 0
        self.family_start = [1, 3, 6, 8, 12]

    def across_time(self,x,y,final=0):
        if not final:
            one_time = x + y
            self.totall_time += one_time
            self.family_start.remove(max(x,y))
            return min(x,y)
        else: self.totall_time += max(x,y)
        return 0


    def first_select_two(self):
      for i in range(len(self.family_start)):
             #print(self.family_start[i])
             for j in range(i+1,len(self.family_start)):
                print(self.family_start[i],self.family_start[j])
                yield self.family_start[i],self.family_start[j]

    def another_one(self,faster):
        for i in range(len(self.family_start)):
            self.across_time(faster,self.family_start[i])


if __name__ == '__main__':
    process = FamilyBridge()

    x,y  = process.first_select_two()
    faster = process.across_time(x,y)
    process.another_one(faster)
