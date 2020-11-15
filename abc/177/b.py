S = input()
T = input()
s_len = len(S)
t_len = len(T)
cnt = t_len
for idx in range(s_len - t_len + 1):
    # print(S[idx:idx+t_len],T)
    tmp_cnt = 0
    for in_idx in range(t_len):
        if T[in_idx] != S[idx + in_idx]:
            tmp_cnt += 1
    if tmp_cnt < cnt:
        cnt = tmp_cnt
print(cnt)
