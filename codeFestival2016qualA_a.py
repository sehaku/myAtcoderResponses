N = int(input())
likes = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if likes[i] == -1:
        continue
    idx = likes[i]-1
    if likes[idx] == i + 1:
        cnt += 1
        likes[idx] = -1
print(cnt)
