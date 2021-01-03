N = int(input())
points = [[0, 0] for _ in range(N)]
for i in range(N):
    x, y = map(int, input().split())
    points[i] = [x, y]
ans = 0
# print(points)
for s in range(N - 1):
    for t in range(s + 1, N):
        if points[s][0] == points[t][0]:
            continue
        elif abs((points[s][1] - points[t][1]) / (points[s][0] - points[t][0])) <= 1:
            ans += 1
print(ans)
