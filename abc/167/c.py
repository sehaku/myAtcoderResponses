def list_add(li1, li2):
    return list(map(sum, zip(li1, li2)))


def dfs(price, knowledge, depth):
    if (min(knowledge) >= X):
        ansList.append(price)
    if depth == N:
        return
    dfs(price, knowledge, depth + 1)
    dfs(price + priceList[depth],
        list_add(KnowList[depth], knowledge), depth + 1)


N, M, X = map(int, input().split(" "))
KnowList = [[] for i in range(N)]
priceList = [0] * N
for i in range(N):
    tmp = [int(i) for i in input().split(" ")]
    priceList[i] = tmp[0]
    KnowList[i] = tmp[1:]
price = 0
ansList = []
knowledge = [0] * M
dfs(price, knowledge, 0)
if (len(ansList) == 0):
    ansList.append(-1)
print(min(ansList))
