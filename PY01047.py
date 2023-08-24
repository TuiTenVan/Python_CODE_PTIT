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
    res = s[-4:]
    if snt(int(res)) == True:
        print("YES")
    else:
        print("NO")

