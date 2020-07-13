N = int(input())
line = [int(i) for i in input().split()]
oddLs = line[0::2]
cnt = 0
for num in oddLs:
    if num % 2 != 0:
        cnt += 1
print(cnt)
