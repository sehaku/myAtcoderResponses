L, R, d = map(int, input().split())
line = [i for i in range(L, R + 1)]
cnt = 0
for num in line:
    if num % d == 0:
        cnt += 1
print(cnt)
