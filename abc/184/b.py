N, X = map(int, input().split())
S = input()
score = X
for i in S:
    if i == "x":
        score = max(0, score - 1)
    else:
        score += 1
print(score)
