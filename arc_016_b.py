buttonType = ['x', 'o', '.']
N = int(input())
line = [list(input()) for _ in range(N)]
buttonTapCnt = 0
for j in range(9):
    longPush = False
    for i in range(N):
        curChar = line[i][j]
        if curChar not in buttonType:
            print(
                "Unexpected Input Char Error at: line[" + str(i) + "][" + str(j) + "] = "+line[i][j])
            exit()
        else:
            if curChar == buttonType[1]:
                if not longPush:
                    longPush = True
                    buttonTapCnt += 1
            else:
                if longPush:
                    longPush = False
                if curChar == buttonType[0]:
                    buttonTapCnt += 1
print(buttonTapCnt)
