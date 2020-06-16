N = list(input())
print(N)
for i in range(len(N) - 1, 0, -1):
    print(N[i])
    if N[i] != '9':
        if 9 - int(N[i]) > 1:
            N[i] = str(9 - int(N[i]))
            N[i - 1] = str(int(N[i - 1]) - 1)
            if N[i - 1] == '-1':
                j = 1
                while N[i-j] == '-1':
                    N[i - j] = '9'
                    N[i-j-1] = str(int(N[i-j-1])-1)
summation = 0
for i in range(len(N)):
    summation += int(N[i])
print(summation)
