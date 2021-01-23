# 0:True,1:False
n = int(input())
s = [""] * n
dp = [[0, 0] for _ in range(n + 1)]
dp[0] = [1, 1]
for i in range(n):
    s[i] = input()
for idx, val in enumerate(s):
    if val == "OR":
        dp[idx + 1][0] = 2 * dp[idx][0] + dp[idx][1]
        dp[idx + 1][1] = dp[idx][1]
    elif val == "AND":
        dp[idx + 1][0] = dp[idx][0]
        dp[idx + 1][1] = 2 * dp[idx][1] + dp[idx][0]
print(dp[-1][0])
