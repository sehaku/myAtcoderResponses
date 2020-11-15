# 2^5000000000000000 > 10^135
S = list(input())
K = int(input())
for i in range(len(S)):
    if S[i] != "1":
        print(S[i])
        exit()
    elif i == K - 1:
        print("1")
        exit()
