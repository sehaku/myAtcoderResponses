INF = 10 ** 10
n, wor = map(int, input().split())
dp = [[INF] * (100001) for _ in range(n + 1)]
dp[0][0] = 0

w = [0]
v = [0]
for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
for i in range(1, len(dp)):
    for j in range(len(dp[0])):
        if j - v[i] >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v[i]] + w[i])
        else:
            dp[i][j] = dp[i - 1][j]


ans = 100000
# print(len(dp), len(dp[0]))
# print(n, wor)
while dp[n][ans] > wor:
    ans -= 1
print(ans)
