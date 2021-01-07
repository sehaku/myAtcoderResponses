n = int(input())
arms = [[0, 0] for _ in range(n)]
for i in range(n):
    x, L = map(int, input().split())
    arms[i][0] = x - L
    arms[i][1] = x + L - 1
arms.sort(key=lambda x: x[1])
now = arms[0][1]
ans = n
for arm in arms[1:]:
    if arm[0] <= now:
        ans -= 1
    else:
        now = arm[1]
print(ans)
