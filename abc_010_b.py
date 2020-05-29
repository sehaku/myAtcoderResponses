# n % 3 == 1 or 0
# n % 2 == 1
N = int(input())
list = [int(i) for i in input().split(' ')]
sum = 0
for i in list:
    for j in range(i):
        if ((i - j) % 3 == 0 or (i - j) % 3 == 1) and (i - j) % 2 == 1:
            sum = sum + j
            break

print(sum)