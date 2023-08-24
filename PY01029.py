def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
t = int(input())
for i in range(t):
    n = input()
    m = int(n)
    dao = 0
    while m > 0:
        dao = dao * 10 + m % 10
        m //= 10
    if gcd(dao, int(n)) == 1:
        print("YES")
    else:
        print("NO")