# print(chr(97))
N = int(input())
lenJudgeNum = [26, 702, 18278, 475254, 12356630, 321272406, 8353082582,
               217180147158, 5646683826134, 146813779479510, 3817158266467286]
alpLen = 0
tmp = N
for i in range(len(lenJudgeNum)):
    if N <= lenJudgeNum[i]:
        alpLen = i + 1
        break

ansStr = ''
prev = 'a'
for i in range(alpLen):
    N -= 1
    alpNum = N % 26
    ansStr = chr(alpNum + 97) + ansStr
    N = N//26
print(ansStr)
