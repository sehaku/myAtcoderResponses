def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


T = int(input())
for i in range(T):
    N, S, K = map(int, input().split())
    d = gcd(gcd(N, N - S), K)
    new_N = N // d
    new_S = (N - S) // d
    new_K = K // d
    if gcd(new_K, new_N) != 1:
        print(-1)
    else:
        print(new_S * pow(new_K, -1, new_N) % new_N)
