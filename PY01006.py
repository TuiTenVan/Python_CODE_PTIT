t = int(input())
for i in range(t):
    x = input()
    ok = 0
    for j in x:
        if j != '4' and j != '7':
            ok = 1
            break
    if ok == 0:
        print("YES")
    else:
        print("NO")