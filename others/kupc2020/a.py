N = int(input())
len_sum = 0

prev = list(map(int, input().split()))

for _ in range(N - 1):
    x, y = map(int, input().split())
    len_sum += abs(prev[0] - x) + abs(prev[1] - y)
    prev = [x, y]
print(len_sum)
