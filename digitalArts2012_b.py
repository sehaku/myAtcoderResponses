instr = input()
line = [i for i in instr]
num = ord('a') - 1
hash = 0
ans = ''
for i in line:
    hash += ord(i) - num
if hash == 26 * 20 or hash == 1:
    print("NO")
else:
    while hash >= 26:
        ans += 'z'
        hash -= 26
    if hash != 0:
        ans += chr(num + hash)
    if line.count('z') == len(line):
        ans = ans[:-1] + 'ya'
    elif instr == ans:
        if len(ans) > 1:
            forward = ans[:-2]
            middle = ans[-2]
            remain = ans[-1]
            ans = forward + remain + middle
        else:
            ans = chr(num+hash-1) + chr(num+1)
    print(ans)
