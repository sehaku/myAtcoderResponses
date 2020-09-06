n, m = map(int, input().split())
dirMax = (n % 12) + (m / 60)
dirMin = m / 5

if dirMax < dirMin:
    dirMax, dirMin = dirMin, dirMax

direct = dirMax - dirMin
indirect = (dirMin + 12) - dirMax
print(min(direct, indirect) * 30)
