n = int(input())
a = list(map(int, input().split()))
tmp = list(range(len(a)))
# print(tmp)
# print(tmp)

while len(tmp) > 2:
    in_tmp = []
    for i in range((len(tmp) // 2)):
        if a[tmp[2 * i]] < a[tmp[2 * i + 1]]:
            in_tmp.append(tmp[2 * i + 1])
        else:
            in_tmp.append(tmp[2 * i])
    tmp = in_tmp[:]

if a[tmp[0]] < a[tmp[1]]:
    print(tmp[0] + 1)
else:
    print(tmp[1] + 1)
