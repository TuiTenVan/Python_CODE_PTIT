t = int(input())

for _ in range(t):
    n, p = list(map(int, input().split()))
    j = 0
    for i in range(2, n + 1):
        while i % p == 0:
            i /= p
            j += 1
    print(j)