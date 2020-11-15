maxColorNum = 8
rates = [False] * maxColorNum
overRed = 0
N = int(input())
people = list(map(int, input().split()))
for i in people:
    idx = i // 400
    if idx >= maxColorNum:
        overRed += 1
    else:
        rates[idx] = True
minNum = 1 if rates.count(True) == 0 and overRed != 0 else rates.count(True)
maxNum = rates.count(True) + overRed

print(str(minNum) + " " + str(maxNum))
