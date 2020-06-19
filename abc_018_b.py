S = list(input())
N = int(input())
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range((tmp[1] - tmp[0] + 1) // 2):
        S[tmp[0] - 1 + j], S[tmp[1] - 1 - j] = S[tmp[1] - 1 - j], S[tmp[0] - 1 + j]
        # print(S)
print("".join(S))
