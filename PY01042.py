t = int(input())
for _ in range(t):
    s = input()
    a = set()
    for j in s:
        a.add(j)
    ok = 0
    for i in a:
        if i != '0' and i != '1' and i != '2':
            ok = 1
            break
    if ok == 1:
        print("NO")
    else:
        print("YES")