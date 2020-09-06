N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            tmp_list = [nums[i], nums[j], nums[k]]
            if i >= j or j >= k:
                continue
            if len(tmp_list) != len(set(tmp_list)):
                continue
            else:
                tmp_list.sort()
                if tmp_list[-1] >= sum(tmp_list[:-1]):
                    continue
                else:
                    cnt += 1
print(cnt)
