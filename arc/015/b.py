N = int(input())
dayType = [0] * 6
for i in range(N):
    query = list(map(float, input().split()))
    if query[0] >= 35:
        dayType[0] += 1
    elif query[0] >= 30:
        dayType[1] += 1
    elif query[0] >= 25:
        dayType[2] += 1
    if query[1] >= 25:
        dayType[3] += 1
    if query[0] >= 0 and query[1] < 0:
        dayType[4] += 1
    if query[0] < 0:
        dayType[5] += 1
print(" ".join(map(str, dayType)))
