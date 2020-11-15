N = input()
N_sum = sum([int(i) for i in N])
if N_sum % 9 == 0:
    print("Yes")
else:
    print("No")
