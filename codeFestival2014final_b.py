S = [int(i) for i in list(input())]
evenNums = S[0::2]
oddNums = S[1::2]
print(sum(evenNums) - sum(oddNums))
