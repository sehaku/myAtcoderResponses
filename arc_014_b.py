# 高橋くんを先攻として交互に与えられる。
N = int(input())
wordList = []
first = input()
wordList.append(first)
lastAlphabet = first[-1]
for i in range(N - 1):
    tmp = input()
    if tmp[0] != lastAlphabet or tmp in wordList:
        print("WIN" if i % 2 == 0 else "LOSE")
        exit()
    wordList.append(tmp)
    lastAlphabet = tmp[-1]
print("DRAW")
