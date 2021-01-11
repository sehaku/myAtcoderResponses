n, prime = map(int, input().split())
services = []
for i in range(n):
    a, b, c = map(int, input().split())
    services.append([a, c])
    services.append([b + 1, -c])
services.sort()

prev_day = 1
price = 0
ans = 0
for idx, service in enumerate(services):

    ans += (service[0] - prev_day) * min(price, prime)
    price += service[1]
    prev_day = service[0]
print(ans)
