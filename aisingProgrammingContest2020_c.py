N = int(input())
ans = [0] * (N + 1)
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            num = pow(x, 2) + pow(y, 2) + pow(z, 2) + \
                (x * y) + (y * z) + (z * x)
            if num <= N:
                ans[num] += 1
for i in ans[1:]:
    print(i)
