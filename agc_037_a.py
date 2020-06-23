S = list(input())
last = ''
cur = ''
ans = 0
for i in range(len(S)):
    cur += S[i]
    if last != cur:
        ans += 1
        last = cur
        cur = ''
print(ans)
