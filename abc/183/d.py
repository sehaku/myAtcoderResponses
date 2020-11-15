N, W = map(int, input().split())
maxlen = 2 * 10 ** 5 + 1
Time = [0] * maxlen
Sum = [0] * maxlen

for _ in range(N):
    S, T, P = map(int, input().split())
    Time[S] += P
    Time[T] -= P
Sum[0] = Time[0]
if Sum[0] > W:
    print("No")
    exit()
for i in range(1, maxlen):
    Sum[i] = Sum[i - 1] + Time[i]
    if Sum[i] > W:
        print("No")
        exit()
print("Yes")
