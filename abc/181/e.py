N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
x_y_between_one = [[0, 0]]
costs = 0

for idx, vals in enumerate(cities[1:]):
    tmp = [pow(cities[0][0] - vals[0], 2) + pow(cities[0][1] - vals[1], 2), idx + 1]
    x_y_between_one.append(tmp)
x_y_between_one.sort()
print(x_y_between_one)
cur_city = cities[0]
cur_city_num = 0
fin_city = [0]

for val in x_y_between_one[1:]:
    nxt_city = cities[val[1]]
    if cur_city_num == 0:
        costs += (
            abs(cur_city[0] - nxt_city[0])
            + abs(cur_city[1] - nxt_city[1])
            + max(0, nxt_city[2] - cur_city[2])
        )
        fin_city.append(val[1])
        print(
            abs(cur_city[0] - nxt_city[0]),
            abs(cur_city[1] - nxt_city[1]),
            max(0, nxt_city[2] - cur_city[2]),
        )
        cur_city = nxt_city
    else:
        min_cost = (
            abs(cur_city[0] - nxt_city[0])
            + abs(cur_city[1] - nxt_city[1])
            + max(0, nxt_city[2] - cur_city[2])
        )
        for idx in fin_city:
            mid_city = cities[idx]
            tmp_cost = (
                abs(cur_city[0] - mid_city[0])
                + abs(cur_city[1] - mid_city[1])
                + max(0, mid_city[2] - cur_city[2])
                + abs(mid_city[0] - nxt_city[0])
                + abs(mid_city[1] - nxt_city[1])
                + max(0, nxt_city[2] - mid_city[2])
            )
            if tmp_cost < min_cost:
                min_cost = tmp_cost
        costs += min_cost


costs += (
    abs(nxt_city[0] - cities[0][0])
    + abs(nxt_city[1] - cities[0][1])
    + max(0, cities[0][2] - nxt_city[2])
)
print(costs)
