import sys
sys.setrecursionlimit(2147483647)


def searchNxt(current, round, isNxtA):
    if isNxtA:
        round += 1
        if current > Aairport[n - 1]:
            print(round)
            exit()
        left = -1
        right = len(Aairport)
        while right - left > 1:
            mid = (right + left) // 2
            if current > Aairport[mid]:
                left = mid
            else:
                right = mid
        searchNxt(Aairport[right] + x, round, False)
    else:
        if current > Bairport[m - 1]:
            print(round)
            exit()
        left = -1
        right = len(Bairport)
        while right - left > 1:
            mid = (right + left) // 2
            if current > Bairport[mid]:
                left = mid
            else:
                right = mid
        searchNxt(Bairport[right] + y, round, True)


# main
n, m = map(int, input().split())
x, y = map(int, input().split())
Aairport = [int(i) for i in input().split()]
Bairport = [int(i) for i in input().split()]
searchNxt(Aairport[0] + x, 0, False)
