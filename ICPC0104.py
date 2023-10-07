def solve(s):
    numbers = []
    s += "@"
    res = ""
    for c in s:
        if c.isdigit():
            res += c
        else:
            if res != "":
                numbers.append(int(res))
                res = ""
    return max(numbers)
t = int(input())
for _ in range(t):
    s = input().strip()
    result = solve(s)
    print(result)