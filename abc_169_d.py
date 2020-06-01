# sqrt(n) <= 10**6 O(√n)ループに耐えうる
# // -> (python 3) 除算の結果をintに
import math
N = int(input())
PrimeFactList = []
tmpNum = N

# 素因数分解
# 2 から順に数字を+1しながら√N + 1まで素因数分解すれば素数以外では素因数分解されない
for i in range(2, int(math.sqrt(N))+1):
    if N % i == 0:
        expcnt = 0
        while tmpNum % i == 0:
            tmpNum //= i
            expcnt += 1
        PrimeFactList.append(i)
        PrimeFactList.append(expcnt)

# 1以外の数が残っていたら足す
if tmpNum != 1:
    PrimeFactList.append(tmpNum)
    PrimeFactList.append(1)

# 素因数が1つもなければN自体を因数に加える
if len(PrimeFactList) == 0:
    PrimeFactList.append(N)
    PrimeFactList.append(1)
ans = 0

if PrimeFactList[0] == 1:
    print(0)
    exit()
# 同じ因数の連続操作に必要な累乗数( opeList[i] = opeList[i-1]+i+1 (*opeList[0]=1))
# 2 ** 40 > 10 ** 12 なのでopeList[i] > 40になった位置までで十分
opeList = [1, 3, 6, 10, 15, 21, 28, 36, 45]
for i in range(1, len(PrimeFactList), 2):
    for j in range(len(opeList)):
        if PrimeFactList[i] < opeList[j]:
            ans += j
            break
print(ans)
