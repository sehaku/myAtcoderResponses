n = int(input())
aoki_sum = 0
lis = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    lis[i] = [2 * a + b, a + b, a]
    aoki_sum += a
lis.sort(reverse=True)
takahashi_sum = 0
idx = 0
# print(lis)
while takahashi_sum <= aoki_sum:
    takahashi_sum += lis[idx][1]
    aoki_sum -= lis[idx][2]
    idx += 1
print(idx)
