n = int(input())
indeed = list("indeednow")
indeed.sort()
ans = []
for i in range(n):
    tmp = list(input())
    tmp.sort()
    if indeed == tmp:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)
