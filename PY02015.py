import math
while True:
    a = list(map(int, input().split()))
    ok = 0
    for i in a:
        if i != 0:
            ok = 1
            break
    if ok == 0:
        break
    cnt = 0
    while a[0] != a[1] or a[1] != a[2] or a[2] != a[3] or a[0] != a[3]:
        x = a[0]
        for i in range(len(a) - 1):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - x)
        # print(str(a[0]) + " " + str(a[1]) + " " + str(a[2]) + " " + str(a[3]))
        cnt += 1
    print(cnt)


