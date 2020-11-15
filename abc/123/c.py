import math

n, a, b, c, d, e = map(int, [input() for i in range(6)])
late = max(
    math.ceil(n / a),
    math.ceil(n / b),
    math.ceil(n / c),
    math.ceil(n / d),
    math.ceil(n / e),
)
print(4 + late)
