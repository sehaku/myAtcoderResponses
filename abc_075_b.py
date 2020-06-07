H, W = map(int, input().split())

field = [list(input()) for _ in range(H)]
directions = [[-1, -1], [-1, 0], [-1, 1],
              [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
for i in range(H):
    for j in range(W):
        if field[i][j] == '.':
            bombCnt = 0
            for k in directions:
                if (i + k[0] >= 0 and i + k[0] < H) and (j + k[1] >= 0 and j + k[1] < W):
                    if field[i + k[0]][j + k[1]] == '#':
                        bombCnt += 1
            field[i][j] = str(bombCnt)
for i in range(H):
    print("".join(field[i]))
