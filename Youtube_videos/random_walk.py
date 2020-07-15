import random

def random_walk(n):
  
  """ Return coordinates after 'n' block random walk."""
  x,y = 0,0
  for i in range(n):
    (dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
    x += dx
    y += dy
  return (x, y)

for i in range(5):
  walk = random_walk(100000)
  print(walk, " Distance from origin = ", abs(walk[0]) + abs(walk[1]))
