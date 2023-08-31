import math
t = int(input())
for _ in range(t):
    n = input()
    m = n[::-1]
    k = math.gcd(int(n), int(m))
    x = int(n) * int(m) // k
    print(m)
    print(k)
    print(x)
