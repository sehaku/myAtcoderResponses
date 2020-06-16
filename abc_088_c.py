import copy

line = [[int(i) for i in input().split()] for _ in range(3)]
ansB = copy.copy(line[0])
ansA = [0, line[1][0]-ansB[0], line[2][0]-ansB[0]]
# print(line, ansA, ansB)
for i in range(1, 3):
    for j in range(1, 3):
        if ansA[i] + ansB[j] != line[i][j]:
            print("No")
            exit()

print("Yes")
