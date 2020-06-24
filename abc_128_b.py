N = int(input())
line = []
for i in range(N):
    tmp = [j for j in input().split()]
    tmp[1] = -1 * int(tmp[1])
    tmp.append(i + 1)
    line.append(tmp)
line.sort()
for i in range(N):
    print(line[i][2])
