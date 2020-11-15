N = int(input())
list = []
count = []
for i in range(N):
    tmp = input()
    if list.count(tmp) != 0:
        idx = list.index(tmp)
        count[idx] = count[idx] + 1
    else:
        list.append(tmp)
        count.append(1)
maxIdx = count.index(max(count))
print(list[maxIdx])
