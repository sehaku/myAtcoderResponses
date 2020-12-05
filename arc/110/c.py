N = int(input())
P = list(map(int, input().split()))
for idx, val in enumerate(P):
    if val == idx + 1:
        print(-1)
        exit()
inc_order = [i for i in range(1, N + 1)]
dictionary = {val: idx for idx, val in enumerate(P)}
current_num = 1
pre_idx = 0
operations = []
while pre_idx != len(P) - 1:
    target_idx = dictionary[current_num]
    for i in range(target_idx - 1, pre_idx - 1, -1):
        P[i], P[i + 1] = P[i + 1], P[i]
        operations.append(i + 1)
    if P[pre_idx:target_idx] != inc_order[pre_idx:target_idx]:
        print(-1)
        exit()
    pre_idx = target_idx
    current_num = target_idx + 1
for i in range(N - 1):
    print(operations[i])

# import random

# length = 10
# randomize = list(range(0, length - 1))
# random.shuffle(randomize)
# shuffled = list(str(i) for i in range(1, length + 1))
# for i in randomize:
#     shuffled[i], shuffled[i + 1] = shuffled[i + 1], shuffled[i]
# print(" ".join(shuffled))
