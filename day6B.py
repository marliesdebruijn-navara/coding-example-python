vProblem = "Guard Gallivant B"
print(vProblem)

# You need to get the guard stuck in a loop by adding a single new obstruction. 
# How many different positions could you choose for this obstruction?

import sys
from copy import deepcopy
sys.setrecursionlimit(10000)

# f = open("examples/example6.txt", "r") 
f = open("input/input6.txt", "r") 
vText = f.read().splitlines()
f.close()
vMap = list(map(list, vText))
vMapNew = deepcopy(vMap)

direction = ["^",">","v","<"]
h = len(vMap[0])
l = len(vMap)

def findStart(element, matrix):
  for i, matrix_i in enumerate(matrix):
    for j, value in enumerate(matrix_i):
      if value == element:
        return (i,j)
      
def turn(i,j,p):
  if vMap[i][j] == direction[p] or vMap[i][j] == "+":
      vMap[i][j] = "+"
      return 1 #found a loop
  else:
    if vMap[j][j] == "<" or vMap[i][j] == ">" or vMap[i][j] == "v" or vMap[i][j] == "^":
      vMap[i][j] = "+" #been here already
    else:
      vMap[i][j] = direction[p] #mark first time
    return move(i,j,p)


def moveUp(i,j):
  vNumOfSteps = 0
  vEnd = False
  vTurn = False
  while not vEnd and not vTurn:
    vNumOfSteps += 1
    if vMap[i-vNumOfSteps][j] == "#":
      vTurn = True 
    else: 
      if vMap[i-vNumOfSteps][j] ==".":
        vMap[i-vNumOfSteps][j] = 'X'
      if i - vNumOfSteps == 0:
        vEnd = True
  if vEnd:
    return 0
  if vTurn:
    return turn(i-vNumOfSteps+1,j,1)

def moveRight(i,j):
  vNumOfSteps = 0
  vEnd = False
  vTurn = False
  while not vEnd and not vTurn:
    vNumOfSteps += 1
    if vMap[i][j+vNumOfSteps] == "#":
      vTurn = True 
    else: 
      if vMap[i][j+vNumOfSteps] ==".":
        vMap[i][j+vNumOfSteps] = 'X'
      if j+vNumOfSteps == l-1:
        vEnd = True
  if vEnd:
    return 0
  if vTurn:
    return turn(i,j+vNumOfSteps-1,2)

def moveDown(i,j):
  vNumOfSteps = 0
  vEnd = False
  vTurn = False
  while not vEnd and not vTurn:
    vNumOfSteps += 1
    if vMap[i+vNumOfSteps][j] == "#":
      vTurn = True 
    else: 
      if vMap[i+vNumOfSteps][j] ==".":
        vMap[i+vNumOfSteps][j] = 'X'
      if i+vNumOfSteps == h-1:
        vEnd = True
  if vEnd:
    return 0
  if vTurn:
    return turn(i+vNumOfSteps-1,j,3)

def moveLeft(i,j):
  vNumOfSteps = 0
  vEnd = False
  vTurn = False
  while not vEnd and not vTurn:
    vNumOfSteps += 1
    if vMap[i][j-vNumOfSteps] == "#":
      vTurn = True 
    else: 
      if vMap[i][j-vNumOfSteps] ==".":
        vMap[i][j-vNumOfSteps] = 'X'
      if j-vNumOfSteps == 0:
        vEnd = True
  if vEnd:
    return 0
  if vTurn:
    return turn(i,j-vNumOfSteps+1,0)

def move(i,j,position):
  if vMap[i][j] == "." : 
    vMap[i][j] = "X"
  match position:
    case 0: #^ i-1
      return moveUp(i,j)
    case 1: #> j+1
      return moveRight(i,j)
    case 2: #v i+1
      return moveDown(i,j)
    case 3: #< j-1
      return moveLeft(i,j)
        
vLoc = findStart("^",vMap)

#find the regular path 
move(vLoc[0],vLoc[1],0)

vSum = 0 
for i in range(len(vMap)):
  vMap[i] = list(map(lambda x: x.replace('+','X').replace('v','X').replace('<','X').replace('^','X').replace('>','X') ,vMap[i] ) )
  vSum += vMap[i].count("X")

print(f"The guard will visit {vSum} positions")

vMap[vLoc[0]][vLoc[1]] = "S"
vMapOrg = deepcopy(vMap)

vCount = 0

#Place the obstacle and check if there is a loop
for i in range(len(vMapOrg)):
  for j in range(len(vMapOrg)):
    if vMapOrg[i][j] != "." and vMapOrg[i][j] != '#' and vMapOrg[i][j] != "S":

      vMap = deepcopy(vMapNew)
      vMap[i][j] = "#"
      vCount +=  move(vLoc[0],vLoc[1],0)

print(f"We can place {vCount} obstacles to create a loop")

sys.setrecursionlimit(1000)