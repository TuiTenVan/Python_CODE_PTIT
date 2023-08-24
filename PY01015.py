t = int(input())
for i in range(t):
    s = input()
    a = []
    ok = 0
    for i in s:
        a.append(i)
    for k in range(len(a) - 1):
        if(a[k] > a[k + 1]):
            ok = 1
            break
    if ok == 0:
        print("YES")
    else:
        print("NO")        