N, K = map(int, input().split())
S = [i for i in input()]
ans = S[:]


def canReplace(i, remain):
    charList = [ans[i + 1]]
    cntList = [1]
    # 文字種とその数を格納
    for j in range(i + 2, N):
        isExist = False
        for k in range(len(charList)):
            if ans[j] == charList[k]:
                cntList[k] += 1
                isExist = True
                break
        if not isExist:
            charList.append(ans[j])
            cntList.append(1)
    # 初期位置と異なるならremainを減らしていく
    for j in S[i + 1 :]:
        try:
            idx = charList.index(j)
            if cntList[idx] <= 0:
                remain -= 1
            else:
                cntList[idx] -= 1
        except:
            remain -= 1
    # remainが残るなら交換可能
    return remain >= 0


for i in range(N - 1):
    ans[i:] = sorted(ans[i:])
    for j in range(i, N):
        # 入れ替えする
        ans[i], ans[j] = ans[i], ans[j]
        remain = K
        if S[i] != ans[i]:
            remain -= 1
        # 入れ替え可能か調べる
        if remain >= 0 and canReplace(i, remain):
            K = remain
            break
        ans[i], ans[j] = ans[j], ans[i]  # 不可能なら戻す
print("".join(ans))
