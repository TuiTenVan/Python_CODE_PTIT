p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    line = input().split()
    if len(line) == 1 and int(line[0]) == 0:
        break
    k, s = line
    k = int(k)
    res = ""
    for j in s:
        x = (p.index(j) + k) % 28
        res += p[x]
    x = res[::-1]
    print(x)