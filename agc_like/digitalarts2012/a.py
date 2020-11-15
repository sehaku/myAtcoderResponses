s = input().split()
N = int(input())
ngwords = [input() for _ in range(N)]
for i in range(len(s)):
    for j in range(len(ngwords)):
        if len(s[i]) != len(ngwords[j]):
            continue
        else:
            if s[i] == ngwords[j]:
                s[i] = "*" * len(s[i])
                break
            for k in range(len(s[i])):
                if s[i][k] != ngwords[j][k] and ngwords[j][k] != "*":
                    break
                if k == len(s[i]) - 1:
                    s[i] = "*" * len(s[i])
print(" ".join(s))
