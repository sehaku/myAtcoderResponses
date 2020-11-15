import itertools

N, K = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(N)]
towns = [i for i in range(1, N + 1)]
p = itertools.permutations(towns, len(towns))
ans = 0
for vals in p:
    if vals[0] != 1:
        break
    in_time = 0
    prev = 1
    for val in vals[1:]:
        in_time += t[prev - 1][val - 1]
        prev = val
    in_time += t[prev - 1][0]
    # print(in_time)
    if in_time == K:
        ans += 1
print(ans)
