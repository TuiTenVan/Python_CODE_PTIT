def sieve(n):
    d = [1] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if d[i] == 1:
            for j in range(i * i, n + 1, i):
                d[j] = 0
    return [i for i in range(2, n + 1) if d[i] == 1]

def check(n, p):
    n = str(n)
    p = str(p)
    return p in n

l, h = map(int, input().split())
p = input()
a = sieve(1000000)
cnt = 0
for x in range(l, h + 1):
    if a[x] >= l and check(a[x], p):
        cnt += 1
print(cnt)
