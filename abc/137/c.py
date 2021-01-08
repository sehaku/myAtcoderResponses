n = int(input())
dic = {}
str_len = 10
for _ in range(n):
    s = sorted(input())
    tmp = "".join(s)
    if tmp in dic.keys():
        num = dic[tmp]
        dic.update({tmp: num + 1})
    else:
        dic.update({tmp: 1})
ans = 0
# print(dic)
for i in dic.values():
    ans += (i * (i - 1)) // 2

print(ans)
"""
1 -> 0 = 0
2 -> 1 = 1
3 -> 2+1 = 3
4 -> 3+2+1 = 6
5 -> 4+3+2+1 = 10
"""
