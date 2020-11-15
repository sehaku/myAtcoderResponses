N = int(input())
s = input()
t = input()
sameLen = 0
for i in range(N):
    if s[i:] == t[: N - i]:
        sameLen = N - i
        break
print(2 * N - sameLen)
