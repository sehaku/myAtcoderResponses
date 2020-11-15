N = int(input())
line = list(map(int, input().split()))
countList = [0] * ((10 ** 5) + 1)

ansSum = sum(line)
for i in line:
    countList[i] += 1
Q = int(input())
for i in range(Q):
    B, C = map(int, input().split())
    ansSum += (C - B) * countList[B]
    countList[C] += countList[B]
    countList[B] = 0
    print(ansSum)
