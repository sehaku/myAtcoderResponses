# 1つ以上は必ず2で割らないと行けない->ai%2==0の要素が少なくとも1つ必要
# odd * 3 => odd, even * 3 => even,3倍の操作で偶奇は入れ替わらない
# ->すべての偶数に対してai/2の操作を繰り返せる回数の合計が最大の操作回数
# 1 000 000 000 < 2^30

N = int(input())
list = [int(i) for i in input().split() if int(i) % 2 == 0]
count = 0
for i in list:  # max 10000 loops
    while i % 2 == 0:  # max 30 loops
        i = i / 2
        count = count + 1
print(count)
# 計算量 O(10 ^ 5)?
