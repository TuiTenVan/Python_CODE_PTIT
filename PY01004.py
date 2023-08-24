import math

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def snt(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    for k in range(1, n):
        if gcd(n, k) == 1:
            cnt += 1
    if snt(cnt):
        print("YES")
    else:
        print("NO")

