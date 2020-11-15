N, M = map(int, input().split())
acCheck = [False] * (N + 1)
waCntList = [0] * (N + 1)
waCnt = 0
for i in range(M):
    query = list(input().split())
    idx = int(query[0])
    if acCheck[idx]:
        continue
    if query[1] == "AC":
        waCnt += waCntList[idx]
        acCheck[idx] = True
    else:
        waCntList[idx] += 1
print(str(acCheck.count(True)), str(waCnt))
