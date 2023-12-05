t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    x = max(a)
    list = []
    for i in range(n):
        if a[i] == x:
            a.insert(i, m)
            break
    for i in a:
        if i < 0:
            list.append(i)
    for i in a:
        if i >= 0 :
            list.append(i)
    for i in list:
        print(i, end=" ")
    print()
