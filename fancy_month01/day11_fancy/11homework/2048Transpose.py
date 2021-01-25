map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]

map1= [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
for xi in range(4):
  #print(xi)
  for yi in range(4):
    map1[yi][xi]= map[xi][yi]
    #print(xi,yi,'正序')
    #print(yi,xi)
   #print(map)
print(map1)

