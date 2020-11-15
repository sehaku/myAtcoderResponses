numbers = [True for i in range(2 * 10 ** 5 + 1)]
N = int(input())
min_num = 0
lis = list(map(int, input().split()))
for val in lis:
    numbers[val] = False
    if val == min_num:
        # min_num = min_num + numbers[min_num:].index(True)

        while not numbers[min_num]:
            min_num += 1
    print(min_num)
