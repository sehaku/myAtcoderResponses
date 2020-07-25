N = int(input())
money = 1000
line = list(map(int, input().split()))
prices = []
increaseFlag = False
decreaseFlag = False
upFlag = False
for cnt, val in enumerate(line):
    if cnt == 0:
        prices.append(val)
    elif prices[-1] == val:
        continue
    elif prices[-1] > val:
        increaseFlag = False
        if len(prices) == 1:
            prices[-1] = val
        else:
            if decreaseFlag:
                prices[-1] = val
            else:
                prices.append(val)
                decreaseFlag = True
    elif prices[-1] < val:
        decreaseFlag = False
        upFlag = True
        if increaseFlag:
            prices[-1] = val
        else:
            prices.append(val)
            increaseFlag = True
if len(prices) == 1:
    print(1000)
elif not upFlag:
    print(1000)
else:
    kabuNum = 0
    leng = len(prices) - (len(prices) % 2)
    for i in range(leng):
        if i % 2 == 0:
            kabuNum = money // prices[i]
            money -= kabuNum * prices[i]
        else:
            money += kabuNum * prices[i]
    print(money)
