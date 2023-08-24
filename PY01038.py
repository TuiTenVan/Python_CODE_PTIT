def check(n):
    dao = 0
    m = n
    while m > 0:
        dao = dao * 10 + m % 10
        m //= 10
    return dao
t = int(input())
for i in range(t):
    n = int(input())
    if(n % 7 == 0):
        print(n)
    else:
        x = check(n)
        while (x + n) % 7 != 0:
            n = x + n
            x = check(n)
        print(n + check(n))
        
    