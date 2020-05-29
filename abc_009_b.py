N = int(input())
list = []
for i in range(N):
    content = int(input())
    if content not in list:
        list.append(content)
list.sort()
print(list[len(list)-2])