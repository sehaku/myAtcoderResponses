# from #15490827
import bisect

def solve(deg1, deg2, lis, magnification):
    tmpAns = 10 ** 10
    for dx in lis[deg1].keys():
        if dx not in lis[deg2].keys():
            continue
        for dy in lis[deg1][dx]:
            t = bisect.bisect_left(lis[deg2][dx], dy)
            if t < len(lis[deg2][dx]):
                tmpAns = min(tmpAns, (lis[deg2][dx][t] - dy) * magnification)
    return tmpAns

N = int(input())
fTof = {"U": {}, "D": {}, "R": {}, "L": {}}
urld = {"U": {}, "D": {}, "R": {}, "L": {}}
ulrd = {"U": {}, "D": {}, "R": {}, "L": {}}
for _ in range(N):
    x, y, u = input().split()
    x = int(x)
    y = int(y)
    if u == "U" or u == "D":
        if x in fTof[u]:
            fTof[u][x].append(y)
        else:
            fTof[u][x] = [y]
    else:
        if y in fTof[u]:
            fTof[u][y].append(x)
        else:
            fTof[u][y] = [x]
    if x+y in urld[u]:
        urld[u][x + y].append(y)
    else:
        urld[u][x + y] = [y]
    if x - y in ulrd[u]:
        ulrd[u][x - y].append(y)
    else:
        ulrd[u][x - y] = [y]

for i in fTof:
    for j in fTof[i]:
        fTof[i][j].sort()
for i in urld:
    for j in urld[i]:
        urld[i][j].sort()
for i in ulrd:
    for j in ulrd[i]:
        ulrd[i][j].sort()
ans = 10**10
ans = min(ans, solve("R", "L", fTof, 5))
ans = min(ans, solve("U", "D", fTof, 5))
ans = min(ans, solve("U", "R", urld, 10))
ans = min(ans, solve("L", "D", urld, 10))
ans = min(ans, solve("U", "L", ulrd, 10))
ans = min(ans, solve("R", "D", ulrd, 10))
print("SAFE" if ans == 10**10 else ans)


'''
# TLE
from collections import deque

sideLen = 200000
def solve_reverse():
    tmpAns = sideLen * 100
    values = []
    for num in range(N):
        if not (U[num] == "R" or U[num] == "L"):
            continue
        else:
            values.append([Y[num], X[num], U[num]])
    values.sort()
    # print(values)
    for num in range(len(values)-1):
        if not (values[num][2] == "R" and values[num + 1][2] == "L") or values[num][0] != values[num+1][0]:
            continue
        else:
            tmpAns = min(tmpAns, values[num + 1][1] - values[num][1])
            #print(1, tmpAns, values[num+1], values[num])
    return tmpAns * 5


def solve_90degree():
    tmpAns = sideLen * 100
    values = []
    for num in range(N):
        if not (U[num] == "R" or U[num] == "U"):
            continue
        else:
            values.append([X[num]+Y[num], X[num], U[num]])
    values.sort()
    for num in range(len(values)-1):
        if not (values[num][2] == "R" and values[num + 1][2] == "U") or values[num][0] != values[num+1][0]:
            continue
        else:
            tmpAns = min(tmpAns, values[num + 1][1] - values[num][1])
            #print(2, tmpAns, values[num+1], values[num])
    return tmpAns * 10


N = int(input())
X = deque()
Y = deque()
U = deque()
def rotate():
    degLis = ["U", "R", "D", "L", "L", "U", "R", "D"]
    for num in range(N):
        tmpX = sideLen - Y[num]
        Y[num] = X[num]
        X[num] = tmpX
        U[num] = degLis[degLis.index(U[num])+4]

for _ in range(N):
    x, y, u = map(str, input().split())
    X.append(int(x))
    Y.append(int(y))
    U.append(u)
ans = sideLen * 100

for i in range(4):
    if i >= 2:
        revNum = solve_reverse()
        ans = min(revNum, ans)
    degNum = solve_90degree()
    ans = min(degNum, ans)
    rotate()

if ans == sideLen * 100:
    print("SAFE")
else:
    print(ans)
'''
