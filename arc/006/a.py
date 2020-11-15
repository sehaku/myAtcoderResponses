winNums = list(map(int, input().split()))
bonus = int(input())
selectNums = list(map(int, input().split()))
sameNumCnt = 0
for num in winNums:
    if num in selectNums:
        sameNumCnt += 1
if sameNumCnt == 6:
    print(1)
elif sameNumCnt == 5:
    if bonus in selectNums:
        print(2)
    else:
        print(3)
elif sameNumCnt <= 2:
    print(0)
else:
    print(8 - sameNumCnt)
