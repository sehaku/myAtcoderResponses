n = int(input())
ans = 0
for i in range(n):
    isum = 0
    start, end = map(int, input().split())
    diff = end - start
    if diff % 2 == 0:
        isum += (start + end) // 2
        isum += (diff // 2) * (start + end)
    else:
        isum += (diff // 2 + 1) * (start + end)
    ans += isum
print(ans)
