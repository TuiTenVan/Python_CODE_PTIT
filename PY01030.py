import math

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
n , k = map(int, input().split())
x = int(pow(10, k) - 1)
y = int(pow(10, k - 1))
cnt = 0
for i in range(y, x):
    if gcd(i, n) == 1:
        if cnt % 10 == 0 and cnt != 0:
            print()
        print(i, end=" ")
        cnt += 1
print()