N, K = map(int, input().split())
score = list(map(int, input().split()))
for i in range(K, N):
    print("Yes" if score[i - K] < score[i] else "No")

"""
# 実直に計算する必要はなかった TLE
from collections import deque

add = deque()
sc = 1
for i in range(K):
    sc *= score[i]
add.append(sc)
for i in range(K, N):
    sc = sc // score[i-K]
    sc *= score[i]
    add.append(sc)
pre = 0
for num, val in enumerate(add):
    if num != 0:
        print("Yes" if val > pre else "No")
    pre = val
"""
