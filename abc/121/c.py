N, M = map(int, input().split())
line = [list(map(int, input().split())) for _ in range(N)]
line.sort()
price = 0
for i in line:
    # print(i, M-i[1])
    if M - i[1] > 0:
        price += i[0] * i[1]
        M = M - i[1]
    elif M - i[1] == 0:
        price += i[0] * i[1]
        break
    else:
        number = i[1] - abs(M - i[1])
        price += i[0] * number
        break
print(price)
