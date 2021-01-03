INF = -1
N = int(input())
dp = [[INF] * 3 for _ in range(N)]
activities = [list(map(int, input().split())) for i in range(N)]
dp[0][0] = activities[0][0]
dp[0][1] = activities[0][1]
dp[0][2] = activities[0][2]
for i in range(1, N):
    dp[i][0] = activities[i][0] + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = activities[i][1] + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = activities[i][2] + max(dp[i - 1][0], dp[i - 1][1])
print(max(dp[-1]))
