vProblem = "Guard Gallivant"
print(vProblem)

# https://adventofcode.com/2024/day/6

# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

# How many distinct positions will the guard visit before leaving the mapped area?

import sys
sys.setrecursionlimit(10000)

# f = open("examples/example6.txt", "r") 
f = open("input/input6.txt", "r") 
vText = f.read().splitlines()
f.close()
vMap = list(map(list, vText))

direction = ["^",">","v","<"]
h = len(vMap[0])
l = len(vMap)

def find(element, matrix):
  for i, matrix_i in enumerate(matrix):
    for j, value in enumerate(matrix_i):
      if value == element:
        return (i,j)
      
def turn(i,j,p):
  vMap[i][j]=direction[p]
  return move(i,j,p)

def move(i,j,position):
  vMap[i][j] = "X"
  match position:
    case 0: #^ i-1
      if i == 0: #move up out of map         
        return True
      else: #move up if not an obstacle   
        if vMap[i-1][j] == "#":
          return turn(i,j,1)
        else:
          return move(i-1,j,0)
    case 1: #> j+1
      if j == l-1: #move right out of map
        return True
      else: #move up if not an obstacle   
        if vMap[i][j+1] == "#":
          return turn(i,j,2)
        else:
          return move(i,j+1,1)
    case 2: #v i+1
      if i == h-1: #move bottom out of map
        return True
      else: #move up if not an obstacle 
        if vMap[i+1][j] == "#":
          return turn(i,j,3)
        else:
          return move(i+1,j,2)
    case 3: #< j-1
      if j == 0: #move left out of map
        return True
      else: #move up if not an obstacle   
        if vMap[i][j-1] == "#":
          return turn(i,j,0)
        else:
          return move(i,j-1,3)

vLoc = find("^",vMap)
move(vLoc[0],vLoc[1],0)
#print(vMap)


vSum = 0 
for i in range(len(vMap)):
  vSum += vMap[i].count("X")

print(f"The guard will visit {vSum} positions")

sys.setrecursionlimit(1000)
