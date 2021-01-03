A, B, C = map(int, input().split())
dp = [[[0] * 102 for _ in range(102)] for _ in range(102)]
dp[A][B][C] = 1
ans = 0
for i in range(A, 101):
    for j in range(B, 101):
        for k in range(C, 101):
            if i == 100 or j == 100 or k == 100:
                ans += dp[i][j][k] * (i - A + j - B + k - C)
                continue
            dp[i + 1][j][k] += (i / (i + j + k)) * dp[i][j][k]
            dp[i][j + 1][k] += (j / (i + j + k)) * dp[i][j][k]
            dp[i][j][k + 1] += (k / (i + j + k)) * dp[i][j][k]

print("{:.9f}".format(ans))
