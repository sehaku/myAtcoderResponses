N, a = map(int, input().split())
k = int(input())
dictionary = [int(i) for i in input().split()]
steps = [0] * (2*N)
steps[0] = a
for i in range(1, 2*N):
    steps[i] = dictionary[steps[i-1] - 1]
if k <= N:
    print(steps[k])
else:
    last_idx = N
    first_idx = N - 1
    while steps[last_idx] != steps[first_idx]:
        first_idx -= 1
    loop_len = last_idx - first_idx
    remain = k % loop_len
    while remain < N:
        remain += loop_len
    print(steps[remain])
