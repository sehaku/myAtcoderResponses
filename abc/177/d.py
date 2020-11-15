from collections import Counter

N, M = map(int, input().split())
groups = [0] * (N + 1)
group_num_list = [[0]]
group_num = 1
for _ in range(M):
    A, B = map(int, input().split())
    if groups[A] != 0 and groups[B] != 0:
        if groups[A] != groups[B]:
            lower = min(groups[A], groups[B])
            higher = max(groups[A], groups[B])
            for i in group_num_list[higher]:
                groups[i] = lower
            tmp = group_num_list[higher]
            group_num_list[lower].extend(tmp)
            # del group_num_list[higher]
    elif groups[A] != 0:
        groups[B] = groups[A]
        group_num_list[groups[A]].append(int(B))
    elif groups[B] != 0:
        groups[A] = groups[B]
        group_num_list[groups[B]].append(int(A))
    else:
        groups[A] = group_num
        groups[B] = group_num
        group_num_list.append([int(A), int(B)])
        group_num += 1
counter = Counter(groups)
# print(collection)
# print(group_num_list)
if len(group_num_list) == 1:
    print(1)
elif int(counter.most_common()[0][0]) != 0:
    print(counter.most_common()[0][1])
else:
    print(counter.most_common()[1][1])
