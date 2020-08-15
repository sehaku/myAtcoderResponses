from collections import defaultdict
N, M = map(int, input().split())
heights = list(map(int, input().split()))
d = defaultdict(list)
for i in range(M):
    A, B = map(int, input().split())
    d[A].append(B)
    d[B].append(A)
ans_cnt = 0
for i in range(1, N + 1):
    if d[i] == []:
        ans_cnt += 1
    else:
        my_height = heights[i - 1]
        flag = True
        for j in d[i]:
            if heights[j - 1] >= my_height:
                flag = False
                break
        if flag:
            ans_cnt += 1
print(ans_cnt)
