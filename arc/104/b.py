# REF = [["A", "T"], ["T", "A"], ["C", "G"], ["G", "C"]]
# N, S = map(str, input().split())
# S = list(S)
# cnt = 0
# for i in range(2, int(N)+1, 2):
#     for j in range(len(S)-i+1):
#         org = S[j : i + j]
#         # ref = S[j : i + j : -1]
#         ref = list(reversed(S[j : i + j]))
#         flag = True
#         # print(i,j,i+j,org, ref)
#         for k in range(len(org)):
#             # print(org[k], ref[len(ref) - k - 1],k,len(ref) - k - 1)
#             if [org[k], ref[k]] not in REF:
#                 flag = False
#                 break
#         if flag:
#             cnt += 1
# print(cnt)
REF = [["A", "T"], ["T", "A"], ["C", "G"], ["G", "C"]]
N, S = map(str, input().split())
S = list(S)
cnt_lis = [[0] * (int(N)+1) for _ in range(4)]  # A T G C
num_alphabet = {"A": 0, "T": 1, "G": 2, "C": 3}
ans = 0
for idx, val in enumerate(S):
    # print(val, num_alphabet[val])
    cnt_lis[num_alphabet[val]][idx + 1] = 1
for num, li in enumerate(cnt_lis):
    tmp = 0
    for idx, val in enumerate(li):
        tmp += val
        cnt_lis[num][idx] = tmp
# print(cnt_lis)
for i in range(1, len(S)+1):
    # print('i',i)
    for j in range(i):
        if (i - j) % 2 != 0:
            continue
        if (
            cnt_lis[0][i] - cnt_lis[0][j] == cnt_lis[1][i] - cnt_lis[1][j]
            and cnt_lis[2][i] - cnt_lis[2][j] == cnt_lis[3][i] - cnt_lis[3][j]
        ):
            # print(S[j:i])
            # print(
            #     i,
            #     j,
            #     "num",
            #     cnt_lis[0][i] - cnt_lis[0][j],
            #     cnt_lis[1][i] - cnt_lis[1][j],
            #     cnt_lis[2][i] - cnt_lis[2][j],
            #     cnt_lis[3][i] - cnt_lis[3][j],
            # )
            flag = True
            org = S[j:i]
            ref = list(reversed(org))
            # print('orgref',org, ref)
            for k in range(len(ref)):
                # print(org[k], ref[k])
                if [org[k], ref[k]] not in REF:
                    flag = False
                    break
            if flag:
                ans += 1
print(ans)
