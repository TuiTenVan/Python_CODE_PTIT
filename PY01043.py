def thuanNghich(n):
    dao = 0
    m = n
    while m > 0:
        dao = dao * 10 + m % 10
        m //= 10
    if dao == n:
        return True
    else:
        return False
def check(n):
    cnt = 0
    while n > 0:
        r = n % 10
        cnt += 1
        if r != 0 and r != 2 and r != 4 and r != 6 and r != 8:
            return False
        n //= 10 
    if cnt % 2 == 0:
        return True
def check1(n):
    while n > 0:
        r = n % 10
        if r % 2 != 0:
            return False
        n //= 10
    return True
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(22, n):
        if check1(j) and check(j) and thuanNghich(j):
            print(j, end=" ")
    print()
        
