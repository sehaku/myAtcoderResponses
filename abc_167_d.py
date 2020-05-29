# 必ずN回以下でループする
N, K = map(int, input().split())
towns = [int(i) for i in input().split()]
arrivedList = [1]
for i in range(N * 2):
    arrivedList.append(towns[arrivedList[-1] - 1])
if K <= N:
    print(arrivedList[K])
    exit()

loop_end = N
loop_start = N - 1
while (arrivedList[loop_end] != arrivedList[loop_start]):
    loop_start -= 1

loop_len = loop_end - loop_start

# Kの値をloop_lenを使って調整する
K = K % loop_len
while K < N:
    K += loop_len

print(arrivedList[K])
