N = int(input())
line = list(input())
rw = {"R": [], "W": []}
ans = N


def replace(c):
    left = -1
    right = len(rw["R"])
    while right - left > 1:
        idx = (right + left) // 2
        if rw["R"][idx] > c:
            right = idx
        else:
            left = idx
    req = len(rw["R"]) - right
    return req


for cnt, i in enumerate(line):
    if i == "R":
        if len(rw["R"]) == 0:
            rw["R"] = [cnt]
        else:
            rw["R"].append(cnt)
    else:
        if len(rw["W"]) == 0:
            rw["W"] = [cnt]
        else:
            rw["W"].append(cnt)
ans = min(len(rw["R"]), len(rw["W"]))
ans = min(ans, replace(len(rw["R"]) - 1))
print(ans)
