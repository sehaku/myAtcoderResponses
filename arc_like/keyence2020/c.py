n, k, s = map(int, input().split())
ans = [(s + 1) % 10 ** 9] * n
ans[:k] = [s] * k
print(" ".join(map(str, ans)))
