N, K = map(int, input().split())
tree = list(map(int, input().split()))
left = 0
right = max(tree)

while right - left > 1:
    cnt = 0
    mid = (right + left) // 2
    for i in tree:
        cnt += i // mid
        if i % mid == 0:
            cnt -= 1  # ちょうどに切れるときは切り口が1減る
    if K >= cnt:
        right = mid
    else:
        left = mid

print(right)
