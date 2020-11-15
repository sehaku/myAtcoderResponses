# print("White" if int(input()) % 2 == 0 else "Black")
points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
d = {}
for point in points:
    d.setdefault(point[0], []).append(point[1])
print(d)
