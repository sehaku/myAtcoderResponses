from heapq import heappop, heappush

n, m = map(int, input().split())
works = [[0, 0] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    works[i][0] = a
    works[i][1] = b
works.sort()
h = []
ans = 0
for i in range(1, m + 1):
    while len(works) > 0 and i >= works[0][0]:
        a, b = works.pop(0)
        heappush(h, -b)
    if h:
        minus_best = heappop(h)
        ans -= minus_best
print(ans)
