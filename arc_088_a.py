N = int(input())
numbers = list(map(int, input().split()))
odd_num_cnt = 0
even_num_cnt = 0
four_mal_cnt = 0
for i in numbers:
    if i % 4 == 0:
        four_mal_cnt += 1
    elif i % 2 == 0:
        even_num_cnt += 1
    else:
        odd_num_cnt += 1
if four_mal_cnt >= odd_num_cnt or (four_mal_cnt == odd_num_cnt - 1 and even_num_cnt == 0):
    print("Yes")
else:
    print("No")
