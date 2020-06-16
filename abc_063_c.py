N = int(input())
questions = []
maxNum = 0
for i in range(N):
    tmp = int(input())
    questions.append(tmp)
questions.sort()
notTenLine = [i for i in questions if i % 10 != 0]
if sum(questions) % 10 != 0:
    print(sum(questions))
elif len(notTenLine) == 0:
    print(0)
else:
    print(sum(questions)-min(notTenLine))
