import math

data = [int(i) for i in input().split(" ")]
canMoveMax = data[4] * data[5]
numOfMomen = int(input())
canGoHouse = False
for i in range(numOfMomen):
    pos = [int(j) for j in input().split(" ")]
    distance = math.sqrt((pos[0] - data[0]) ** 2 + (pos[1] - data[1]) ** 2) + math.sqrt(
        (data[2] - pos[0]) ** 2 + (data[3] - pos[1]) ** 2
    )
    if not canGoHouse and distance <= canMoveMax:
        canGoHouse = True
if canGoHouse:
    print("YES")
else:
    print("NO")
