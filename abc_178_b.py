a, b, c, d = map(int, input().split())
max_val = -10 ** 18
for i in [a, b]:
    for j in [c, d]:
        if i * j > max_val:
            max_val = i * j
print(max_val)
