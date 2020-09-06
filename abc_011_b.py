S = input()
ans = ""
loop = 0
for i in S:
    if loop == 0:
        ans = ans + i.upper()
    else:
        ans = ans + i.lower()
    loop = loop + 1
print(ans)
