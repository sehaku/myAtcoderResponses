numbers = [
    [[".###", ".#.#", ".#.#", ".#.#", ".###"], "0"],
    [["..#.", ".##.", "..#.", "..#.", ".###"], "1"],
    [[".###", "...#", ".###", ".#..", ".###"], "2"],
    [[".###", "...#", ".###", "...#", ".###"], "3"],
    [[".#.#", ".#.#", ".###", "...#", "...#"], "4"],
    [[".###", ".#..", ".###", "...#", ".###"], "5"],
    [[".###", ".#..", ".###", ".#.#", ".###"], "6"],
    [[".###", "...#", "...#", "...#", "...#"], "7"],
    [[".###", ".#.#", ".###", ".#.#", ".###"], "8"],
    [[".###", ".#.#", ".###", "...#", ".###"], "9"],
]
N = int(input())
S = [input() for _ in range(5)]
ans = ""
for i in range(N):
    tmp = [
        S[0][4 * i : 4 * (i + 1)],
        S[1][4 * i : 4 * (i + 1)],
        S[2][4 * i : 4 * (i + 1)],
        S[3][4 * i : 4 * (i + 1)],
        S[4][4 * i : 4 * (i + 1)],
    ]
    for i in numbers:
        if tmp == i[0]:
            ans += i[1]
print(ans)
