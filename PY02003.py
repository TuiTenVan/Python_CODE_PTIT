import math
def snt(n):
    if n < 2: 
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    n = int(input())
    max_snt = -1
    for i in range(0, int(math.sqrt(n)) + 1):
        if snt(i) and int(n) % i == 0:
            max_snt = max(max_snt, i)
    if max_snt > 5:
        print("Not in sequence")
    else:
        print(max_snt)