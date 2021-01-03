N, W = map(int, input().split())
FIRST = 0
weights = [0]
values = [0]
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
dp = [[FIRST] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(W + 1):
        if j - weights[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[-1][-1])
