#Greedy Method
def greed():
  r = [[1,2],[4,3],[7,5]]
  g = [[6,5],[7,8],[2,1]]
  b = [[7,5],[1,4],[1,3]]
  house = [[-1,-1],[-1,-1],[-1,-1]]
  for i in range(0,3):
    for j in range(0,2):
      fillcolor(house,r,g,b,i,j)

  for i in range(0,len(house)):
    print(house[i])

def fillcolor(house,r,g,b,row,col): 
  color = [0,1,2]
  if(row == 0):
    if(col - 1 >= 0):
      c = house[row][col -1]
      color.remove(c)
      house[row][col] = min_color(color,r,g,b,row,col)
    if(col == 0):
      house[row][col] = min_color(color,r,g,b,row,col)
  else:
    if(col - 1 >= 0):
      c1 = house[row-1][col]
      c2 = house[row][col-1]
      if(row == 2):
        c3 = house[row-2][col]
        color.remove(c3)
        if(c1 != c3):
          color.remove(c1)
        if(c2 != c3 and c2 != c1):
          color.remove(c2)
      else:
        color.remove(c1)
        if (c1 != c2):
          color.remove(c2)
    house[row][col] = min_color(color,r,g,b,row,col)
    if(col == 0):
      c1 = house[row-1][col]
      color.remove(c1)
      house[row][col] = min_color(color,r,g,b,row,col)

def min_color(color,r,g,b,row,col):
  cost = []
  for j in range(0,len(color)):
    cost.append(-1)
  for i in range(0,len(color)):
    if(color[i] == 0):
      cost[i] = r[row][col]
    if(color[i] == 1):
      cost[i] = g[row][col]
    if(color[i] == 2):
      cost[i] = b[row][col]
  mval = min(cost)
  k = cost.index(mval)
  return color[k]


greed()
