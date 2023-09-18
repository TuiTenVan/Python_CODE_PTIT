with open("CONTACT.in", "r") as contact:
    s = {}
    for x in contact:
        if x[-1] == '\n':
            x = x[:-1]
        s[x.lower()] = 1
    s = sorted(s.keys())
    for x in s:
        print(x)