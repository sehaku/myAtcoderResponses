def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


N = int(input())
lis = [i for i in range(2, N + 1, 1)]
ans = lis[0]
for i in lis[1:]:
    ans = lcm(ans, i)
print(int(ans) + 1)
# import random

# length = 10
# randomize = list(range(0, length - 1))
# random.shuffle(randomize)
# shuffled = list(str(i) for i in range(1, length + 1))
# for i in randomize:
#     shuffled[i], shuffled[i + 1] = shuffled[i + 1], shuffled[i]
# print(" ".join(shuffled))
