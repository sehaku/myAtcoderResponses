INF = 10 ** 10
N = int(input())
heights = list(map(int, input().split()))
dp = [INF] * N
dp[0] = 0
for i in range(N):
    if i + 1 < N:
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(heights[i + 1] - heights[i]))
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(heights[i + 2] - heights[i]))
print(dp[-1])
