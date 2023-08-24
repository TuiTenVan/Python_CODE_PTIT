import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n, k = map(int, input().split())
arr = []
cnt = 0
i = 0
while cnt != n:
    if snt(i):
        arr.append(i)
        cnt += 1
    i += 1
b = []
b.append(k)
for i in arr:
    b.append(b[-1] + i)
for x in b:
    print(x, end=" ")
print()

