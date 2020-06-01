A, B, C, D = map(int, input().split())
rateTaka = B / A
rateAoki = D / C
if rateTaka == rateAoki:
    print("DRAW")
elif rateTaka > rateAoki:
    print("TAKAHASHI")
else:
    print("AOKI")
