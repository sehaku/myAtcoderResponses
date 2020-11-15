X, Y, A, B = map(int, input().split())
exp = 0
a = A
if Y <= X * A and Y <= X + B:
    print(0)
    exit()
while Y > X * pow(a, exp + 1):
    exp += 1
b_only_exp = (Y - X) // B if (Y - X) % B != 0 else (Y - X) // B - 1
if exp > b_only_exp:
    print(exp)
else:
    exp = 0
    a = A
    while B > X * pow(a, exp + 1):
        exp += 1
    print(b_only_exp + exp)
