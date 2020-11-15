# 偶数-> E869120 君,奇数-> square1001 君と決め打ち
# -> 各々8切れより多くは取れない
wantToEat = [int(i) for i in input().split(" ")]
if wantToEat[0] > 8 or wantToEat[1] > 8:
    print(":(")
else:
    print("Yay!")
