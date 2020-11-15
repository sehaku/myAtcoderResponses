import itertools

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
comb = itertools.combinations(points, 3)
for val in comb:
    dx1 = val[0][0] - val[1][0]
    dy1 = val[0][1] - val[1][1]
    dx2 = val[0][0] - val[2][0]
    dy2 = val[0][1] - val[2][1]
    if dy1 * dx2 == dy2 * dx1:
        print("Yes")
        exit()
print("No")
