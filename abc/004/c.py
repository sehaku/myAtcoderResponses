N = int(input())
line = ["1", "2", "3", "4", "5", "6"]
idx = (N // 5) % 6
line = line[idx:] + line[:idx]
# print(line)
insert_idx = (N % 5) + 1
line.insert(insert_idx, line[0])
del line[0]
print("".join(line))
