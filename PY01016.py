import math

t = int(input())
for i in range(t):
    s = input()
    res = s[0]
    for j in range(1, len(s)):
        if s[j].isdigit() and int(s[j]) > 0 and int(s[j]) < 10:
            for k in range(1, int(s[j])):
                res += s[j - 1]
        else:
            res += s[j]
    print(res)
