S = input()
T = input()
wildCard = list("atcoder")
canWin = True
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif (S[i] == "@" and T[i] in wildCard) or (T[i] == "@" and S[i] in wildCard):
        continue
    else:
        canWin = False
        break
print("You can win" if canWin else "You will lose")
