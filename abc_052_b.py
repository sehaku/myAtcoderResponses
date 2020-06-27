N = int(input())
line = list(input())
maxNum = 0
cur = 0
for i in line:
    if i == 'I':
        cur += 1
    else:
        cur -= 1
    maxNum = max(maxNum, cur)
print(maxNum)
