import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum(n):
    tong = 0
    for i in range(2, n + 1):
        if is_prime(i) and n % i == 0:
            tong += i
            if(is_prime(n // i) and n % i == 0):
                tong += n // i
    return tong

N = int(input())
total = 0
for _ in range(N):
    num = int(input())
    total += sum(num)
print(total)
