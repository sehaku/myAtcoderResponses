N = int(input())
ans = 0
for i in range(1, N + 1):
    if "7" in str(i):
        ans += 1
        continue
    if "7" in format(i, "o"):
        ans += 1
        continue
print(N - ans)
