N = int(input())
buttons = [0] * (N + 1)
for i in range(N):
    buttons[i + 1] = int(input())
current = 1
for i in range(N):
    current = buttons[current]
    if current == 2:
        print(i + 1)
        exit()
print(-1)
