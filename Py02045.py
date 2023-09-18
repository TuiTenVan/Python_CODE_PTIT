s = input()
while len(s) > 0:
    a = s[0:len(s) // 2]
    b = s[len(s) // 2:]
    if a != "" and b != "":
        x = int(a) + int(b)
        print(x)
        s = str(x)
    else:
        break
