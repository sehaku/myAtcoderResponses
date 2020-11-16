N, M, Q = map(int, input().split())
graph = {}
for i in range(M):
    u, v = map(int, input().split())
    current = []
    if u in graph:
        current = graph[u]
    current.append(v)
    graph.update({u: current})
    current = []
    if v in graph:
        current = graph[v]
    current.append(u)
    graph.update({v: current})
colors = [-100] + list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))
    color = colors[query[1]]
    print(color)
    if query[0] == 1:
        if query[1] in graph:
            for idx in graph[query[1]]:
                colors[idx] = color
    else:
        colors[query[1]] = query[2]
