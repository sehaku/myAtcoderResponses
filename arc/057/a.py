A, K = list(map(int, input().split()))
days = 0
if K != 0:
    while A < 2 * (10 ** 12):
        A = A + 1 + (K * A)
        days += 1
else:
    days = 2 * (10 ** 12) - A
print(days)
