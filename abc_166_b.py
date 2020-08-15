N, K = map(int, input().split())
have_sweets = []
for i in range(K):
    d = int(input())
    have_sweets += list(map(int, input().split()))
have_sweets = set(have_sweets)
print(len(list(set([i for i in range(1, N+1)])-have_sweets)))
