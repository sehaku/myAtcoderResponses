# list[1]の数にlist[1]回100をかければよいはず
list = [int(i) for i in input().split(" ")]
fillzero = 0
plus = 0
if list[0] == 0:
    fillzero = 1
    plus = 1
elif list[0] == 1:
    fillzero = 100
    plus = 100
elif list[0] == 2:
    fillzero = 10000
    plus = 10000
if list[1] != 100:
    print(list[1] * fillzero)
else:
    print((list[1] * fillzero)+plus)
# max 2 100 -> 1000000 (intで表現可能)
