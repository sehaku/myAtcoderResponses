import math

N = int(input())
S = [set(list(input())) for _ in range(N)]
forward = ""
slen = len(S)
loop = math.floor(slen / 2)
for i in range(loop):
    if S[i] & S[slen - i - 1]:
        forward += (S[i] & S[slen - i - 1]).pop()
    else:
        print(-1)
        exit()
ans = ""
if slen % 2 == 0:
    ans = forward + forward[::-1]
else:
    ans = forward + S[loop].pop() + forward[::-1]
print(ans)
