import math
hourR, minR, H, M = map(int, input().split())
hourPos = [math.sin(((H * 60 + M) / 360) * math.pi) * hourR,
           math.cos(((H * 60 + M) / 360) * math.pi) * hourR]
minPos = [math.sin((M / 30) * math.pi) * minR,
          math.cos((M / 30) * math.pi) * minR]
distance = math.sqrt(
    pow(hourPos[0] - minPos[0], 2) + pow(hourPos[1] - minPos[1], 2))
print(distance)
