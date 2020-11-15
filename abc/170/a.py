line = list(map(int, input().split()))
for i in range(5):
    if line[i] != i + 1:
        print(i + 1)
        exit()
