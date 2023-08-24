def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

t = int(input())
for _ in range(t):
    a = int(input())
    b = int(input())
    result = gcd(a, b)
    print(result)
