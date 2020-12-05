fox = []
N = int(input())
S = input()
S_len = len(S)
cnt = S_len
for idx, char in enumerate(S):
    if char == "f":
        fox.append(char)
    elif char == "o":
        if len(fox) == 0:
            continue
        if fox[-1] == "f":
            fox.append(char)
        else:
            fox = []
    elif char == "x":
        if len(fox) < 2:
            fox = []
        else:
            char1, char2 = fox.pop(), fox.pop()
            if char1 == "o" and char2 == "f":
                cnt -= 3
            else:
                fox = []
    else:
        fox = []
print(cnt)
