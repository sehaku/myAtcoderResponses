X, K, D = map(int, input().split())
if abs(X) < abs(X - D) and abs(X) < abs(X + D):
    if K % 2 == 0:
        print(abs(X))
    else:
        print(min(abs(X - D), abs(X + D)))
else:
    if abs(X - D) < abs(X + D):
        if K * D <= abs(X):
            print(abs(X - (K * D)))
        else:
            remain = K - (abs(X) // D)
            X = X - (abs(X) // D) * D
            if remain % 2 == 0:
                print(abs(X))
            else:
                print(abs(X - D))
    elif abs(X - D) >= abs(X + D):
        if K * D <= abs(X):
            print(abs(X + (K * D)))
        else:
            remain = K - (abs(X) // D)
            X = X + (abs(X) // D) * D
            if remain % 2 == 0:
                print(abs(X))
            else:
                print(abs(X + D))
