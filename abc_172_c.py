N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_sum = [0]
b_sum = [0]
for val in A:
    a_sum.append(a_sum[-1] + val)
for val in B:
    b_sum.append(b_sum[-1] + val)

ans = 0
b = M
for a in range(N + 1):
    if a_sum[a] > K:
        break
    while b_sum[b] > K - a_sum[a]:
        b -= 1
    ans = max(ans, a + b)
print(ans)
