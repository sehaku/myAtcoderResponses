N = int(input())
numbers = [0] * (10 ** 6)
seq = list(map(int, input().split()))
for i in seq:
    numbers[i - 1] += 1
    numbers[i] += 1
    numbers[i + 1] += 1
print(max(numbers))

'''
# method of using collections most_common
import copy
import collections
N = int(input())
seq = [int(i) for i in input().split()]
seqP1 = [i + 1 for i in copy.copy(seq)]
seqM1 = [i - 1 for i in copy.copy(seq)]
mixed = seq + seqM1 + seqP1
print(mixed.count(collections.Counter(mixed).most_common()[0][0]))
'''
