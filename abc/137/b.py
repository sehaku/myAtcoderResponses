k, x = map(int, input().split())
left = x - k + 1
right = x + k
lis = range(left, right)
print(" ".join(map(str, lis)))
