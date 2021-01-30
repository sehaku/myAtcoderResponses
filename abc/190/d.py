def prime_fact(n):
    prime = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            prime.append(i)
            if i != n // i:
                prime.append(n // i)
        i += 1
    return prime


n = int(input())
ans = 0
for div in prime_fact(n):
    if n % div == 0 and (n // div) % 2 == 1:
        ans += 2
print(ans)
