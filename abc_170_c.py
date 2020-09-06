X, N = map(int, input().split())
line = list(map(int, input().split()))
notLine = [i for i in range(-100, 201) if i not in line]
left = -1
right = len(notLine)
while abs(right - left) > 1:
    middle = (right + left) // 2
    if notLine[middle] >= X:
        right = middle
    else:
        left = middle
# print(notLine[left], notLine[right])
if X - notLine[left] <= notLine[right] - X:
    print(notLine[left])
else:
    print(notLine[right])
