N = int(input())
currentTime = 0
current = [0, 0]
for i in range(N):
    timeStamp = list(map(int, input().split()))
    reqLen = abs(timeStamp[1] - current[0]) + abs(timeStamp[2] - current[1])
    timeLen = timeStamp[0] - currentTime
    if reqLen > timeLen:
        print("No")
        exit()
    if reqLen % 2 != timeLen % 2:
        print("No")
        exit()
    currentTime = timeStamp[0]
    current = timeStamp[1:]
print("Yes")
