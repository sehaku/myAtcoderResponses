N = int(input())
line = list(map(int, input().split()))
if line.count(0) != 0:
    print(0)
    exit()
max = 10**18
ans = 1
for i in range(N):
    ans *= line[i]
    if ans > max:
        ans = -1
        break
print(ans)
