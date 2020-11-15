N, M = map(int, input().split())
start_nums = [0] + list(map(int, input().split()))
target_nums = [0] + list(map(int, input().split()))
graph = [[] for _ in range(M + 1)]
canGoToTarget = False
if sum(start_nums) != sum(target_nums):
    canGoToTarget = False
else:
    diff = [y - x for (x, y) in zip(start_nums, target_nums)]
    for _ in range(M):
        c, d = map(int, input().split())
        graph[c].append(d)
        graph[d].append(c)
    for i in range(1, M):
        diff[i]
print("Yes" if canGoToTarget else "No")
