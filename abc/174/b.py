N, D = map(int, input().split())
cnt = 0
for i in range(N):
    X, Y = map(int, input().split())
    if D ** 2 >= X ** 2 + Y ** 2:
        cnt += 1
print(cnt)
