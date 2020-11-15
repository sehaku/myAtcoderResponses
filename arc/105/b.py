def gcd(prev, now):
    while prev > 0:
        tmp = now % prev
        now = prev
        prev = tmp
    return now


N = int(input())
numset = set(map(int, input().split()))
numbers = list(numset)
# numbers.sort()
prev = numbers[0]
for i in numbers[1:]:
    prev = gcd(prev, i)
print(prev)
# while numbers[0] != numbers[-1]:
#     numbers[-1] -= numbers[0]
#     if numbers[-1] < numbers[0]:
#         tmp = numbers[-1]
#         del numbers[-1]
#         numbers.insert(0, tmp)
#     if numbers[-1] == numbers[-2]:
#         del numbers[-1]
#     elif numbers[-1] < numbers[-2]:
#         i = -2
#         while numbers[-1] >= numbers[i]:
#             i -= 1
#         tmp = numbers[-1]
#         del numbers[-1]
#         if tmp != numbers[i]:
#             numbers.insert(i + 1, tmp)
# print(numbers[0])
