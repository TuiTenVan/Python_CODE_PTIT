t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ok = True
    arr1 = sorted(a)
    arr2 = sorted(b)
    for i in range(n):
        if arr1[i] > arr2[i]:
            ok = False
            break
    if ok == True:
        print("YES")
    else:
        print("NO")
    t -= 1
