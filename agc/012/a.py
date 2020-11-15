N = int(input())
members = list(map(int, input().split()))
members.sort()
ans = 0
for i in range(N):
    ans += members[len(members) - (i * 2 + 2)]
print(ans)
