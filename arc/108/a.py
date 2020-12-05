S, P = map(int, input().split())
i = 1
low, up = [], []
while i ** 2 <= P:
    if P % i == 0:
        low.append(i)
        if i != P // i:
            up.append(P // i)
    i += 1
if len(up) != len(low) and low[-1] * 2 == S:
    print("Yes")
    exit()

for j in range(len(up)):
    if low[j] + up[j] == S:
        print("Yes")
        exit()
print("No")
