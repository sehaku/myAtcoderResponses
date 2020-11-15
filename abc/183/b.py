sx, sy, gx, gy = map(int, input().split())
a = (gy + sy) / (gx - sx)
x = sx + (sy / a)
print(x)
