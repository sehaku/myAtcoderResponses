K = int(input())
s = 7
digit = 1
for i in range(K): # Mod KはK種類しかない
    if s % K == 0:
        break
    digit += 1
    s = int(str(s) + '7') % K #余りで計算してもMod Kの値は変わらない
if s % K == 0:
    print(digit)
else:
    print(-1)
