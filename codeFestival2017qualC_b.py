N = int(input())
original = list(map(int, input().split()))
odd = [i for i in original if i % 2 != 0]
ans = 3 ** (len(original))
if len(odd) != len(original):
    ans -= 2**(len(original)-len(odd))
else:
    ans -= 1
print(ans)
