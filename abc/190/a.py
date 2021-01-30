a, b, c = map(int, input().split())
li = [a, b]
while True:
    if li[c] <= 0:
        break
    li[c] -= 1
    c = (c + 1) % 2
print("Takahashi" if c == 1 else "Aoki")
