import math

list = [0] * 290
N = int(input())
for i in range(N):  # O(7n)
    tmp = [int(i) for i in input().split("-")]
    tmp[0] = tmp[0] - (tmp[0] % 5)
    if tmp[1] % 5 != 0:
        tmp[1] = tmp[1] + 5 - (tmp[1] % 5)
    start = math.floor(tmp[0] / 100) * 12 + math.floor((tmp[0] % 100) / 5)
    stop = math.floor(tmp[1] / 100) * 12 + math.floor((tmp[1] % 100) / 5)
    list[start] = list[start] + 1
    list[stop] = list[stop] - 1
flag = True
num = 0
sum = 0
str = ""
for i in range(len(list)):
    sum = sum + list[i]
    if flag and sum >= 1:
        flag = False
        # 1ごとに5増加
        # 12ごとに100増加,60減少
        num = math.floor(i / 12) * 100 + (i % 12) * 5
        str = "{0:04d}".format(num)
    if not flag and sum == 0:
        flag = True
        num = math.floor(i / 12) * 100 + (i % 12) * 5
        str = str + "-" + "{0:04d}".format(num)
        print(str)
        str = ""
