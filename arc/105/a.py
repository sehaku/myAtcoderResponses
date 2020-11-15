# cookies = list(map(int, input().split()))
# sum_of_deli = sum(cookies)
# if sum_of_deli % 2 != 0:
#     print("No")
# else:
#     half = False
#     for i in range(len(cookies)):
#         if sum_of_deli == 2 * cookies[i]:
#             half = True
#         for j in range(i + 1, len(cookies)):
#             if sum_of_deli == 2 * (cookies[i] + cookies[j]):
#                 half = True
#             for k in range(j + 1, len(cookies)):
#                 if sum_of_deli == 2 * (cookies[i] + cookies[j] + cookies[k]):
#                     half = True
#     print("Yes" if half else "No")
import numpy as np

l = [1, 2, 3]
l[1:2] += 1
print(l)
