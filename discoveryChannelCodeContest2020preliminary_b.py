N = int(input())
sticks = list(map(int, input().split()))
sticksSum = sum(sticks)
diffMin = sum(sticks)
plusSticks = 0
for i in range(len(sticks)):
    plusSticks += sticks[i]
    diffMin = min(diffMin, abs(2*plusSticks-sticksSum))
print(diffMin)
