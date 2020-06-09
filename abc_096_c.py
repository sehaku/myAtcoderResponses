H, W = map(int, input().split())
canvas = [[i for i in input()]]
for i in range(H - 1):
    tmp = [i for i in input()]
    canvas.append(tmp)
direction = [[-1, 0], [0, -1], [0, 1], [1, 0]]
for i in range(H):
    for j in range(W):
        if canvas[i][j] == "#":
            canDraw = False
            for k in direction:
                if (i - k[0] >= 0 and i - k[0] < H) and (j - k[1] >= 0 and j - k[1] < W):
                    if canvas[i - k[0]][j - k[1]] == "#":
                        canDraw = True
                        break
            if not canDraw:
                print("No")
                exit()
print("Yes")
