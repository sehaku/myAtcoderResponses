N = int(input())
ans = []
back = []
for i in range(1, int(pow(N, 0.5)) + 1):
    if N % i == 0:
        ans.append(i)
        if i * i != N:
            back.append(N // i)
ans = ans + back[::-1]
for i in ans:
    print(i)
