line = list(map(int, input().split()))
if line[1] % 2 != 0:
    print("No")
elif line[0] * 4 >= line[1] and line[0] * 2 <= line[1]:
    print("Yes")
else:
    print("No")
