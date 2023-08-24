import math
def gcd(a, b):
    while(b > 0):
        a, b = b, a % b
    return a
def snt(a):
    if(a < 2):
        return False
    for i in range(2, int(math.sqrt(a))) :
        if a % i == 0:
            return False
    return True
def check(a):
    sum = 0
    while a > 0:
        sum += a % 10
        a //= 10
    return sum
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    x = gcd(a, b)
    k = check(x)
    if snt(k):
        print("YES")
    else:
        print("NO")
