s = input()
t = input()
s = "1" + s
t = "2" + t
dp = [[0] * (len(t)) for _ in range(len(s))]
for i in range(1, len(s)):
    for j in range(1, len(t)):
        if s[i] == t[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
i_now = len(s) - 1
j_now = len(t) - 1
len_now = dp[i_now][j_now]
ans = ""
while len_now > 0:
    if s[i_now] == t[j_now]:
        ans = s[i_now] + ans
        i_now -= 1
        j_now -= 1
        len_now -= 1
    elif dp[i_now][j_now] == dp[i_now - 1][j_now] and i_now - 1 >= 0:
        i_now -= 1
    else:
        j_now -= 1
print(ans)
