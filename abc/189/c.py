# stack使ってMax rectangleを求める O(2n)
n = int(input())
a = list(map(int, input().split()))
top = 0
max_area = 0
stack = []
for i in range(n):
    '''
    a[i]>=a[stack[-1]] (広義単調増加)ならstackにindexを追加して次へ
    そうでないならa[i]>=a[stack[-1]]になるかstackがなくなるまでrectangleを計算する
    rectangleの計算:stackは広義単調増加なので、popする前のstack[-2]より右はa[stack[-1]]の高さのrectangleになる
    したがってa[stack[-1]] * (index - stack[-2] -1)
    stackが一つしか無いときa[stack[-1]]はindexまでの全区間で最小なのでa[stack[-1]]の高さのrectangleになる
    したがってa[stack[-1]] * index
    '''
    if len(stack) == 0 or a[stack[-1]] <= a[i]:
        stack.append(i)
    else:
        while len(stack) > 0 and a[stack[-1]] >= a[i]:
            tmp = stack.pop()
            if len(stack) != 0:
                max_area = max(max_area, a[tmp] * (i - stack[-1] - 1))

            else:
                max_area = max(max_area, a[tmp] * i)
        stack.append(i)
'''
残ったstackに対してもrectangleを計算する
ただし最後までstackにpushした後なのでindexはlen(a)になる
'''
i = len(a)
while len(stack) > 0:
    tmp = stack.pop()
    if len(stack) != 0:
        max_area = max(max_area, a[tmp] * (i - stack[-1] - 1))
    else:
        max_area = max(max_area, a[tmp] * i)


print(max_area)


#  愚直解:O(n^2)
'''
n = int(input())
a = list(map(int, input().split()))
ans = 0
for left in range(n):
    cur = a[left]
    for right in range(left, n):
        if a[right] < cur:
            cur = a[right]
        ans = max(ans, cur * (right - left + 1))
print(ans)
'''
