# second AC method
S = input()
T = input()
a_idx = ord('a')
S_Lis = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [],
         13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: []}
T_Lis = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [],
         13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: []}
leng = len(S)
for i in range(leng):
    S_Lis[ord(S[i]) - a_idx].append(i)
    T_Lis[ord(T[i]) - a_idx].append(i)
if sorted(S_Lis.values()) == sorted(T_Lis.values()):
    print("Yes")
else:
    print("No")


'''
# first AC method
S = input()
T = input()
a_idx = ord('a')
S_Lis = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [],
         13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: []}
T_Lis = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [],
         13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: [], 22: [], 23: [], 24: [], 25: []}
leng = len(S)
for i in range(leng):
    S_Lis[ord(S[i]) - a_idx].append(i)
    T_Lis[ord(T[i]) - a_idx].append(i)

for i in range(26):
    tmpS = S_Lis[i]
    if len(tmpS) == 0 or tmpS == T_Lis[i]:
        continue
    else:
        flag = True
        for j in T_Lis.values():
            if tmpS == j:
                flag = False
                break
        if flag:
            print("No")
            exit()
print("Yes")
'''


'''
# using collections.Counter method (firstest, 3rd AC)

import collections
S = list(input())
T = list(input())
if sorted(collections.Counter(S).values()) == sorted(collections.Counter(T).values()):
    print("Yes")
else:
    print("No")
'''
