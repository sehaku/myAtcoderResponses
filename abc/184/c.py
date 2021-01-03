r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if r1 == r2 and c1 == c2:
    print(0)
elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
    print(1)
else:
    r2 -= r1
    c2 -= c1
    r2 = abs(r2)
    c2 = abs(c2)
    if (r2 == 0 and c2 <= 6) or (c2 == 0 and r2 <= 6):
        print(2)
    elif r2 % 2 == c2 % 2:
        print(2)
    elif abs(r2 - c2) <= 3:
        print(2)
    else:
        print(3)
