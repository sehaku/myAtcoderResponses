a, b = map(int, input().split())
print(max(sum(list(map(int, str(a)))), sum(list(map(int, str(b))))))
