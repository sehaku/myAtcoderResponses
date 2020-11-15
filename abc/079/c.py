def calc(summation, step, operation):
    if step < len(line):
        # plus
        calc(summation + line[step], step + 1, operation + "+")
        # minus
        calc(summation - line[step], step + 1, operation + "-")
    if step == len(line):
        if summation == 7:
            ans = (
                str(line[0])
                + operation[0]
                + str(line[1])
                + operation[1]
                + str(line[2])
                + operation[2]
                + str(line[3])
                + "=7"
            )
            print(ans)
            exit()


line = [int(i) for i in input()]
calc(line[0], 1, "")
