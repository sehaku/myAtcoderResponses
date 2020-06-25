A, B = map(int, input().split())
B = B // 4 - B // 100 + B // 400
A = (A - 1) // 4 - (A - 1) // 100 + (A - 1) // 400
print(B - A)
