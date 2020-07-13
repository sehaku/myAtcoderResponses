'''
AC x C
WA x C
TLE x C
RE x C
'''
types = ['AC', 'WA', 'TLE', 'RE']
cntLn = [0] * 4
N = int(input())
for i in range(N):
    tmp = input()
    try:
        idx = types.index(tmp)
        cntLn[idx] += 1
    except ValueError as err:
        print("This is value error. -> ", err)
        exit()
for num, value in enumerate(types):
    print(value, "x", str(cntLn[num]))
