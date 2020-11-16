A, R, N = map(int, input().split())
ans = A
idx = 1
if R == 1:
    print(A)
    exit()
while ans <= 10 ** 9:
    if idx == N:
        print(ans)
        exit()
    ans *= R
    idx += 1

print("large")
