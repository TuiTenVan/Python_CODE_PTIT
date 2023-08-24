def count(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    return cnt
t = int(input())
for i in range(t):
    X = int(input()) 
    n = X
    while True:
        k = count(n)
        ok = True
        for i in range(1, n):
            if k <= count(i):
                ok = False
                break
        if ok == True:
            print(n)
            break
        else:
            n += 1

    