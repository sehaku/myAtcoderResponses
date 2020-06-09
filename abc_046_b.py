import math
N, K = map(int, input().split())
ans = K
ans *= pow(K - 1, N - 1)
print(ans)
