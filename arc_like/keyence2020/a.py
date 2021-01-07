h = int(input())
w = int(input())
n = int(input())
if h > w:
    h, w = w, h
print(-(-n // w))
