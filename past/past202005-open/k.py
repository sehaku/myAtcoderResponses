N, Q = map(int, input().split())
down = [-100] * (N + 1)
top = [i for i in range(N + 1)]
ans = [-100] * (N + 1)
for _ in range(Q):
    f, t, x = map(int, input().split())
    tmp = top[f]
    top[f] = down[x]
    top[t], tmp = tmp, top[t]
    down[x] = tmp
for idx, val in enumerate(top):
    if val == -100:
        continue
    else:
        tmp = val
        ans[tmp] = idx
        while down[tmp] != -100:
            tmp = down[tmp]
            ans[tmp] = idx
for i in ans[1:]:
    print(i)
