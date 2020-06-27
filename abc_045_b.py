S = []
for i in range(3):
    tmp = list(input())
    S.append(tmp)
turn = 0
while True:
    if len(S[turn]) == 0:
        print(chr(ord('A')+turn))
        break
    next = ord(S[turn][0]) - ord('a')
    del S[turn][0]
    turn = next
