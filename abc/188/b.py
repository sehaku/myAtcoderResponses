n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for first, second in zip(a, b):
    ans += first * second
print("Yes" if ans == 0 else "No")
