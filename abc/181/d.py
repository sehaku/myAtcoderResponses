import itertools
import collections

div = 8
s = int(input())
if s < 10:
    print("Yes" if s == div else "No")
elif s < 100:
    if s % div == 0 or (10 * (s % 10) + (s // 10)) % div == 0:
        print("Yes")
    else:
        print("No")
else:
    # lis = list(set(list(str(n))).sort()
    strs = list(str(s))
    # lis = [int(i) for i in list(set(strs))]
    counter = collections.Counter(strs)
    lis = []
    for key in counter.keys():
        tmp = [int(key)] * min(3, counter[key])
        lis += tmp

    for vals in itertools.permutations(lis, 3):
        if (100 * vals[0] + 10 * vals[1] + vals[2]) % div == 0:
            print("Yes")
            exit(0)
    # print(100 * vals[0] + 10 * vals[1] + vals[2])
    print("No")
