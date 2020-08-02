'''
    √a+√b < √c
    a+b+2√ab < c
    2√ab < c-a-b
    if c-a-b > 0:
        4ab < (c-a-b)**2
    else:
        not √a+√b < √c
'''
a, b, c = map(int, input().split())
if c - a - b > 0 and 4 * a * b < (c - a - b) ** 2:
    print("Yes")
else:
    print("No")
