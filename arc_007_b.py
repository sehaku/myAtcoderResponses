N, M = map(int, input().split())
disks = [i + 1 for i in range(N)]
nowPlaying = 0
for i in range(M):
    next = int(input())
    if next == nowPlaying:
        continue
    idx = disks.index(next)
    disks[idx], nowPlaying = nowPlaying, disks[idx]

for i in range(N):
    print(disks[i])
