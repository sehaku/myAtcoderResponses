choku = ["c", "h", "o", "k", "u"]
S = input()
isChoku = True
cCounter = 0
for i in range(len(S)):
    if S[i] not in choku:
        isChoku = False
        break
    elif S[i] == "c":
        if isChoku:
            isChoku = False
        else:
            break
    elif S[i] == "h":
        if not isChoku:
            isChoku = True
        else:
            isChoku = False
            break
    elif not isChoku:
        break

print("YES" if isChoku else "NO")
