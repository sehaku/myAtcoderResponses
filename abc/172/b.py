S = input()
T = input()
ans = 0
for idx in range(len(S)):
    if S[idx] != T[idx]:
        ans += 1
print(ans)
