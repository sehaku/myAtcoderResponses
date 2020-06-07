N = int(input())
S = list(input())
maxCommon = 0
for i in range(1, N):
    commonNum = len(list(set(S[0:i]) & set(S[i:])))
    if commonNum > maxCommon:
        maxCommon = commonNum

print(maxCommon)
'''
# C-like answer
N = int(input())
S = list(input())
maxCommon = 0
for i in range(1, N):
    count = 0
    for j in range(ord('a'), ord('z')+1):
        left = False
        right = False
        for k in range(i):
            if ord(S[k]) == j:
                left = True
        for k in range(N - 1, i - 1, -1):
            if ord(S[k]) == j:
                right = True
        if right and left:
            count += 1
    if maxCommon < count:
        maxCommon = count
print(maxCommon)
'''
