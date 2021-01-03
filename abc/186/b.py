H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
min_num = 1000
for i in a:
    min_num = min(min_num, min(i))
ans = 0
for line in a:
    for val in line:
        ans += val - min_num
print(ans)
