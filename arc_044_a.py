import math

N = int(input())
isPrime = True
if N == 1:
    isPrime = False
elif N == 2:
    isPrime = True
else:
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        if N % i == 0:
            isPrime = False
    if not isPrime:
        if N % 2 == 0 or N % 5 == 0:
            isPrime = False
        else:
            digitSum = 0
            for i in range(len(str(N))):
                digitSum += int(str(N)[i])
            if digitSum % 3 != 0:
                isPrime = True
            else:
                isPrime = False
ans = "Prime" if isPrime else "Not Prime"
print(ans)
