n, m = map(int, input().split())
pairs = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
selections = [list(map(int, input().split())) for _ in range(k)]

nodes = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for pair in pairs:
    nodes[pair[0]][pair[1]] += 1
    nodes[pair[1]][pair[0]] += 1

ans = 0
for bit in range(2 ** k):
    select = []
    for i in range(k):
        if (bit >> i) & 1:
            select.append(selections[i][1])
        else:
            select.append(selections[i][0])
    select = list(set(select))
    now = 0
    for idx, a in enumerate(select[:-1]):
        for b in select[idx + 1 :]:
            now += nodes[a][b]
    ans = max(ans, now)
print(ans)
