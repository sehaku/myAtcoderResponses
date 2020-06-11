N, A, B = map(int, input().split())
distance = abs(A - B)
if distance % 2 == 1:
    print(min(A - 1, N - B) + 1 + (distance - 1) // 2)
else:
    print(distance // 2)
