N = int(input())
points = list(map(int, input().split()))
manhattan = 0
euclid = 0
chebyshev = 0
for val in points:
    manhattan += abs(val)
    euclid += pow(abs(val), 2)
    chebyshev = max(chebyshev, abs(val))
euclid = pow(euclid, 0.5)
print(manhattan)
print(euclid)
print(chebyshev)
