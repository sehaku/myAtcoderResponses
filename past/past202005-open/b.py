N, M, Q = map(int, input().split())
Solved = {}
Scores = [N] * (N + 1)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        ans = 0
        lis = []
        if query[1] in Solved:
            lis = Solved[query[1]]
            for val in lis:
                ans += Scores[val]
            print(ans)
        else:
            print(0)
    else:
        Scores[query[2]] -= 1
        current = []
        if query[1] in Solved:
            current = Solved[query[1]]
        current.append(query[2])
        Solved.update({query[1]: current})
