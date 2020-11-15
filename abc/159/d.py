from collections import Counter

# import time

# start = time.time()
N = int(input())
line = list(map(int, input().split()))
# dic = set(line)
dic = Counter(line)
nums = 0
for num, cnt in dic.items():
    if cnt > 1:
        nums += (cnt * (cnt - 1)) // 2
for i in line:
    print(nums - (dic[i] - 1))
"""
for i in dic:
    cnt = line.count(i) - 1
    nums += (cnt * (cnt + 1)) // 2

for i in line:
    cnt = line.count(i) - 1
    print(nums - cnt)

end = time.time()
print(end-start)
"""
