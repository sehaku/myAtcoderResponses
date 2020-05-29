from collections import OrderedDict
from decimal import Decimal, ROUND_HALF_UP
degree = OrderedDict([(11.25, 'N'), (33.75, "NNE"), (56.25, "NE"), (78.75, "ENE"), (101.25, "E"), (123.75, "ESE"), (146.25, "SE"), (168.75, "SSE"),
                      (191.25, "S"), (213.75, "SSW"), (236.25, "SW"), (258.75, "WSW"), (281.25, "W"), (303.75, "WNW"), (326.25, "NW"), (348.75, "NNW"), (361, "N")])
# degree = {11.25: 'N', 33.75: "NNE", 56.25: "NE", 78.75: "ENE", 101.25: "E", 123.75: "ESE", 146.25: "SE", 168.75: "SSE",
#          191.25: "S", 213.75: "SSW", 236.25: "SW", 258.75: "WSW", 281.25: "W", 303.75: "WNW", 326.25: "NW", 348.75: "NNW", 361: "N"}
wind = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6]
list = input().split()
deg = float(list[0])/10
dis = float(Decimal(str(int(list[1]) / 60)
                    ).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
ansdeg = ""
answind = 0
for i in degree:
    if i > deg:
        ansdeg = degree[i]
        break
for i in range(len(wind)):
    if wind[i] > dis or wind[i] == dis:
        answind = i
        if i == 0:
            ansdeg = "C"
        break
    if i == len(wind) - 1:
        answind = len(wind)
print(ansdeg, answind)
