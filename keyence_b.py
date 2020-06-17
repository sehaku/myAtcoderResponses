S = list(input())
for i in range(len(S)):
    for j in range(len(S)):
        tmp = S[:i] + S[j:]
        if ''.join(tmp) == 'keyence':
            print("YES")
            exit()
print("NO")
