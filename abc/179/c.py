# My answer
import math

N = int(input())
cnt = 0
for i in range(1, int(math.sqrt(N)) + 1):
    for j in range(1, N // i + 1):
        if i * j < N:
            if i == j:
                cnt += 1
            elif i < j:
                cnt += 2
print(cnt)

"""
# (Probably) fastest answer
n = int(input())
print(sum([(n - 1) // i for i in range(1, n)]))
"""
