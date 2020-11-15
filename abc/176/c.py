N = int(input())
A = list(map(int, input().split()))
previous = A[0]
stand_sum = 0
for i in A[1:]:
    if i < previous:
        stand_sum += previous - i
    else:
        previous = i
print(stand_sum)
