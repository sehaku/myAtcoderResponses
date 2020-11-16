N, W = map(int, input().split())
maxlen = 2 * 10 ** 5 + 1
Sum = [0] * maxlen

for _ in range(N):
    S, T, P = map(int, input().split())
    Sum[S] += P
    Sum[T] -= P
for i in range(maxlen):
    if i != 0:
        Sum[i] += Sum[i - 1]
    if Sum[i] > W:
        print("No")
        exit()
print("Yes")
