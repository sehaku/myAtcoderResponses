s = input()
k = int(input())
parts = set()
if k > len(s):
    print(0)
    exit()
for idx in range(k, len(s) + 1):
    parts.add(s[idx - k:idx])
# print(parts)
print(len(parts))
