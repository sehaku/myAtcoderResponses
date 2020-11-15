N, M, K = map(int, input().split())
follow = [[i] for i in range(N + 1)]
timeLineCnt = [0] * (N + 1)
eachCnt = [0] * (N + 1)
for i in range(M):
    query = input().split()
    if query[0] == "t":
        eachCnt[int(query[1])] += 1
    # フォロー時のカウント分を減らして、アンフォロー時のカウント分を増やす(差分を取る)
    elif query[0] == "f":
        timeLineCnt[int(query[1])] -= eachCnt[int(query[2])]
        timeLineCnt[int(query[2])] -= eachCnt[int(query[1])]
        follow[int(query[1])].append(int(query[2]))
        follow[int(query[2])].append(int(query[1]))
    elif query[0] == "u":
        timeLineCnt[int(query[1])] += eachCnt[int(query[2])]
        timeLineCnt[int(query[2])] += eachCnt[int(query[1])]
        follow[int(query[1])].remove(int(query[2]))
        follow[int(query[2])].remove(int(query[1]))
# フォローが外れていない人(自分自身含)のつぶやきを増やす
for i in range(1, N + 1):
    for j in follow[i]:
        timeLineCnt[j] += eachCnt[i]
timeLineCnt.sort()
print(timeLineCnt[-K])
