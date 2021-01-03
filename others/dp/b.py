INF = 10 ** 10
N, K = map(int, input().split())
heights = list(map(int, input().split()))
dp = [INF] * N
dp[0] = 0

for i in range(N):
    for j in range(1, K + 1):
        if i + j >= N:
            break
        dp[i + j] = min(dp[i + j], dp[i] + abs(heights[i + j] - heights[i]))

print(dp[-1])
