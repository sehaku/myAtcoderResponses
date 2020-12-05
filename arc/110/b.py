import math


N = int(input())
S = input()
S_len = len(S)
max_len = 10 ** 10
if "110" in S:
    first_110_idx = S.index("110")
    # if (first_110_idx == 1 and S[0] != '0') or (first_110_idx == 2 and S[0:2] != '10'):
    #     print(0)
    #     exit()
    num_of_110 = math.floor((S_len - first_110_idx) / 3)
    if num_of_110 != S.count("110"):
        print(0)
        exit()
    rem = (S_len - first_110_idx) % 3
    # if (rem == 1 and S[-1] != '1') or (rem == 2 and S[-2:] != '11'):
    #     print(0)
    #     exit()
    if rem == 0 and first_110_idx == 0:
        print(max_len - (num_of_110 - 1))
    elif rem != 0 and first_110_idx != 0:
        print(max_len - (num_of_110 + 1))
    else:
        print(max_len - (num_of_110))
else:
    if S_len == 1:
        print(2 * max_len if S == "1" else max_len)
    elif S_len == 2:
        if S == "11" or S == "10":
            print(max_len)
        elif S == "01":
            print(max_len - 1)
        else:
            print(0)
    elif S_len == 3:
        if S == "101" or S == "011":
            print(max_len - 1)
        else:
            print(0)
    elif S_len == 4:
        if S == "1011":
            print(max_len - 1)
        else:
            print(0)
    else:
        print(0)
