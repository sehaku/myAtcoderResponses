S = input()
for i in range(1, len(S)):
    if (len(S) - i) % 2 == 0:
        tmp = S[: len(S) - i]
        left = tmp[: len(tmp) // 2]
        right = tmp[len(tmp) // 2 :]
        if left == right:
            print(len(S) - i)
            exit()
print(0)
