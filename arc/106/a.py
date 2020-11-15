# 8,4,2,6
# 3,9,27,81,243,729,
N = int(input())
if N % 2 != 0 or N % 10 == 0:
    print(-1)
    exit()
for three in range(1, 38):
    for five in range(1, 26):
        if 3 ** three + 5 ** five == N:
            print(three, five)
            exit()
print(-1)
