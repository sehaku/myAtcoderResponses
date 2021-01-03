N = int(input())
exclamations = set()
normal = set()
for _ in range(N):
    s = input()
    if s[0] == "!":
        exclamations.add(s[1:])
        if s[1:] in normal:
            print(s[1:])
            exit()
    else:
        normal.add(s)
        if s in exclamations:
            print(s)
            exit()
print("satisfiable")
