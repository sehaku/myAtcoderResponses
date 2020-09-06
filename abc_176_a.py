import math

N, X, T = map(int, input().split())
times = math.ceil(N / X)
print(times * T)
