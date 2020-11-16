N, L = map(int, input().split())

lis = list(map(int, input().split()))
hurdles = [False] * (L + 1)
for i in lis:
    hurdles[i] = True
dp = [10 ** 9] * (L + 1)
T = list(map(int, input().split()))

for i in range(L):
    if i == 0:
        dp[i] = 0

    dp[i + 1] = min(
        dp[i + 1], dp[i] + T[0] if not hurdles[i + 1] else dp[i] + T[0] + T[2]
    )
    if i + 2 <= L:
        dp[i + 2] = min(
            dp[i + 2],
            dp[i] + T[0] + T[1] if not hurdles[i + 2] else dp[i] + T[0] + T[1] + T[2],
        )
    else:
        dp[L] = min(dp[L], dp[i] + (T[0] + T[1]) // 2)
    if i + 4 <= L:
        dp[i + 4] = min(
            dp[i + 4],
            dp[i] + T[0] + 3 * T[1]
            if not hurdles[i + 4]
            else dp[i] + T[0] + 3 * T[1] + T[2],
        )
    else:
        dp[L] = min(dp[L], dp[i] + (T[0] // 2) + (L - i - 1) * T[1] + (T[1] // 2))
print(dp[L])
