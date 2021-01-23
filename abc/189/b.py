n, x = map(int, input().split())
handrad_x = 100 * x
cur = 0
for i in range(n):
    v, p = map(int, input().split())
    cur += v * p
    if cur > handrad_x:
        print(i + 1)
        exit()
print(-1)
