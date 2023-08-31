t = int(input())
for _ in range(t):
    s = input()
    t = s.split()
    res = ""
    for i in t:
        if i != "and" and i != "of" and i != "in":
            res += i[0].upper()
    print(res, s)
