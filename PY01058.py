import math
def snt(n):
    if n < 2: 
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    s = input()
    ok = 0
    x = s[-4:]
    if snt(int(x)):
        print("YES")
    else:
        print("NO")
