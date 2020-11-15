card_num = 100
in_lis = [list(map(int, input().split())) for _ in range(card_num)]
for idx in range(card_num):
    in_lis[idx].append(idx)
in_lis.sort(key=lambda n: (n[0], n[1] if n[0] % 2 == 0 else -n[1]))
x = 10
y = 0
# u, d, l, r = [0, -1], [0, 1], [-1, 0], [1, 0]
operation = []
have = []
x_pos = 0
next_id = 0
for col_x in range(20):
    tmp = []
    while in_lis[next_id][0] == col_x and col_x != 19:
        have.append(in_lis[next_id][2])
        tmp.append(in_lis[next_id][1])
        next_id += 1
    if col_x % 2 == 0:
        max_x = max(in_lis[next_id - 1][1], in_lis[next_id][1])
        for i in tmp:
            operation += ["R"] * (i - x_pos) + ["I"]
            x_pos = i
        operation += ["R"] * (max_x - x_pos)
        operation.append("D")
        x_pos = max_x
    else:
        if col_x != 19:
            min_x = min(in_lis[next_id - 1][1], in_lis[next_id][1])
            for i in tmp:
                operation += ["L"] * (x_pos - i) + ["I"]
                x_pos = i
            operation += ["L"] * (x_pos - min_x)
            operation.append("D")
        else:
            for j in in_lis[next_id:]:
                have.append(j[2])
                tmp.append(j[1])
            for i in tmp:
                operation += ["L"] * (x_pos - i) + ["I"]
                x_pos = i
                y = x_pos
            if x_pos > 10:
                operation += ["L"] * (x_pos - 10)
                y = x_pos - 10
        x_pos = min_x

# operation += ["U"] * 19
new_lis = []
card_id = 99
for in_x in range(10):
    for in_y in range(10):
        operation += ["O"]
        if in_y != 9:
            if in_x % 2 == 0:
                operation.append("R")
            else:
                operation.append("L")
        new_lis += [
            [19 - in_x, in_y + y if in_x % 2 == 0 else 9 - in_y + y, have[card_id]]
        ]
        card_id -= 1
    if in_x != 9:
        # operation += "D"
        operation += "U"
new_lis.sort(key=lambda n: n[2])
for idx, pos in enumerate(new_lis):
    dis_x = pos[0] - x
    dis_y = pos[1] - y
    x_cnt = 0
    if dis_x < 0:
        operation += ["U"] * abs(dis_x)
        x += dis_x
    else:
        operation += ["D"] * abs(dis_x)
        x += dis_x
    if dis_y < 0:
        operation += ["L"] * abs(dis_y)
        y += dis_y
    else:
        operation += ["R"] * abs(dis_y)
        y += dis_y
    operation += ["I"]
print("".join(operation))
