N, Y = map(int, input().split())
if Y % 1000 != 0:
    print(-1, -1, -1)
else:
    # max(N)=2000 -> 2000**2 = 4*(10**6)
    for a in range(N + 1):
        for b in range(N + 1):
            c = N - a - b
            if c < 0:
                continue
            elif Y == 10000 * c + 5000 * b + 1000 * a:
                print(c, b, a)
                exit()
    print(-1, -1, -1)
