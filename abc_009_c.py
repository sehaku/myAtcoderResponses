# Wrong Answer

import copy
numbers = [int(i) for i in input().split(' ')]
str = input()
strList = []  # 実際に並び替える
for i in str:
    strList.append(i)
parent = copy.copy(strList)  # 並び替え数参照用
smallest = copy.copy(strList)  # 辞書順最小
smallest.sort()
for i in range(len(strList)):  # O(7 * 100)= 700 ^ 2 = 490000 = 4.9 * 10^5
    # print(numbers[1])
    if strList[i] == smallest[i]:
        continue
    else:
        comparedList = copy.copy(strList)  # 差分比較用
        changeChar = strList[i]
        targetIdx = strList.index(smallest[i])
        comparedList[targetIdx] = changeChar
        comparedList[i] = smallest[i]
        diffCount = 0
        for j in range(len(comparedList)):
            if comparedList[j] != parent[j]:
                diffCount = diffCount + 1
        if diffCount <= numbers[1]:
            strList = copy.copy(comparedList)

print(''.join(strList))
