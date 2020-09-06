list = [int(i) for i in input().split(" ")]
sum = 0
if list[0] < list[3]:
    sum = list[0]
    if list[0] + list[1] < list[3]:
        minus = list[3] - list[1] - list[0]
        sum = sum - minus
else:
    sum = list[3]
print(sum)
