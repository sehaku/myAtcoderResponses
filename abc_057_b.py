# manhattan distance |x1-x2|+|y1-y2|
def list_add(l1, l2):
    tmp = [abs(a-b) for a, b in zip(l1, l2)]
    return tmp


N, M = map(int, input().split())
students = [[int(i) for i in input().split()] for _ in range(N)]
checkpoints = [[int(i) for i in input().split()] for _ in range(M)]

for i in students:
    cur_point = 0
    min_point = 1
    smallest = sum(list_add(i, checkpoints[0]))
    for j in checkpoints:
        cur_point += 1
        sum_li = sum(list_add(i, j))
        if sum_li < smallest:
            smallest = sum_li
            min_point = cur_point
    print(min_point)
