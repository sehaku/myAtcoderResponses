A, B = map(str, input().split())
pattern = [
    ["9" + A[1:], B],
    [A[0] + "9" + A[2], B],
    [A[:-1] + "9", B],
    [A, "1" + B[1:]],
    [A, B[0] + "0" + B[2]],
    [A, B[:-1] + "0"],
]
maxNum = -10000
for i in pattern:
    tmp = int(i[0]) - int(i[1])
    if maxNum < tmp:
        maxNum = tmp
print(maxNum)
