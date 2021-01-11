INF = 10 ** 20
ans = -INF
n, m = map(int, input().split())
gold_prices = list(map(int, input().split()))
paths = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    paths[y - 1].append(x - 1)
dp = [INF for _ in range(n)]
for i in range(n):
    tmp_min = INF
    if len(paths[i]) > 0:
        tmp_min = min(dp[j] for j in paths[i])
    ans = max(ans, gold_prices[i] - tmp_min)
    dp[i] = min(tmp_min, gold_prices[i])
print(ans)
