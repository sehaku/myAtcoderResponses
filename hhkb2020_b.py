H, W = map(int, input().split())
field = [input() for _ in range(H)]
ans = 0
for lis in field:
    flag = False
    for val in lis:
        if val == ".":
            if not flag:
                flag = True
            else:
                ans += 1
        else:
            flag = False
for i in range(W):
    flag = False
    for j in range(H):
        if field[j][i] == ".":
            if not flag:
                flag = True
            else:
                ans += 1
        else:
            flag = False

print(ans)
