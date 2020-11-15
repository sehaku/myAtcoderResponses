
import itertools
n, m = map(int, input().split())
w = list(map(int, input().split()))
per = itertools.permutations(w)
bridge = [list(map(int, input().split())) for _ in range(m)]
for val in per:
    print(val)
for bri in bridge:
    l, v = map(int, bri)
    if v > sum_w:
        continue
    if v < max_w:
        print(-1)
        exit()
