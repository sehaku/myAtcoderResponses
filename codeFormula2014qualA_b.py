a, b = map(int, input().split())
throw1 = [int(i) - 1 for i in input().split()]
throw2 = [int(i) - 1 for i in input().split()]
if throw1.count(-1) != 0:
    throw1[throw1.index(-1)] = 9
if throw2.count(-1) != 0:
    throw2[throw2.index(-1)] = 9
line = ["x"] * 10
for i in throw1:
    line[i] = "."
for i in throw2:
    line[i] = "o"
ans1 = line[6] + " " + line[7] + " " + line[8] + " " + line[9]
ans2 = " " + line[3] + " " + line[4] + " " + line[5]
ans3 = "  " + line[1] + " " + line[2]
ans4 = "   " + line[0]
print(ans1)
print(ans2)
print(ans3)
print(ans4)
