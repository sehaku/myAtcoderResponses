# Wrong Answer


import sys

sys.setrecursionlimit(1000000)


def search(currentPos, stepCount):
    if currentPos == targetPos and stepCount == list[0]:
        arrivalCount.append(1)
    if stepCount != list[0]:
        for i in range(4):
            px = currentPos[0] + dx[i] * list[1]
            py = currentPos[1] + dy[i] * list[1]
            search([px, py], stepCount + 1)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
list = [int(i) for i in input().split(" ")]
targetPos = [int(i) for i in input().split(" ")]
possibility = 0.0
stepCount = 0
arrivalCount = []
if list[1] % 2 == 0 and (targetPos[0] % 2 == 1 or targetPos[1] % 2 == 1):
    possibility = 0.0
elif list[1] % 2 == 1 and (targetPos[0] % 2 == 0 or targetPos[1] % 2 == 0):
    possibility = 0.0
else:
    search([0, 0], stepCount)
    if arrivalCount.count == 0:
        print(0.0)
        exit()
    else:
        possibility = sum(arrivalCount) / pow(4, list[0])
print(possibility)
