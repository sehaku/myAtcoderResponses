sizePrice = list(map(int, input().split()))
N = int(input())
oneLMin = min([sizePrice[0] * 4, sizePrice[1] * 2, sizePrice[2]])
twoLMin = min([oneLMin*2, sizePrice[3]])
ans = 0
if N % 2 == 0:
    ans = twoLMin * (N//2)
else:
    ans = twoLMin * ((N - 1)//2) + oneLMin
print(ans)
