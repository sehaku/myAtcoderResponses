X, Y = map(int, input().split())
twoLine = [X*(2 ** i) for i in range(61)]

for i in range(len(twoLine)):
    if X * twoLine[i] > Y:
        print(i)
        exit()
