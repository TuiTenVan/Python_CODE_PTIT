t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())
    a1 = sorted(a)
    b1 = sorted(b)
    i = 0
    j = 0
    ok = 0
    while i < n or j < n:
        if a1[i] <= b1[j]:
            i += 1
            j += 1
        else:
            ok = 1
            break
    if ok == 0:
        print("YES")
    else:
        print("NO")