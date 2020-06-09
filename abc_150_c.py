'''
1, 2, 3, 4, 5
1, 2, 4, 3, 5
1, 2, 4, 5, 3
1, 2, 5, 3, 4
1, 2, 5, 4, 3
1, 3, 2, 4, 5
'''


def exclude(cs, s):
    return [x for i, x in enumerate(cs) if i not in s]


def createLine(line, length):
    if length <= 0 or length > len(line):
        return []
    result = []
    _createLine(line, length, [], result)
    return result


def _createLine(line, length, progress, result):
    if length == 0:
        result.append(progress)
        return

    for i in range(len(line)):
        _createLine(exclude(line, [i]), length - 1,
                    progress + [line[i]], result)


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
line = [i for i in range(1, N + 1)]
string = createLine(line, N)
print(abs(string.index(Q)-string.index(P)))
