import math
H, W = map(int, input().split())
if H == 1 or W == 1:
    print(1)
    exit()
print((H // 2) * (W // 2) + (H // 2 + H % 2) * (W // 2 + W % 2))
