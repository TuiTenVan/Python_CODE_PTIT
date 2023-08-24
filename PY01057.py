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
    for j in range(0, len(s)):
        if (snt(j) and snt(int(s[j])) == False) or (snt(j) == False and snt(int(s[j]))):
            ok = 1
            break
    if ok == 1:
        print("NO")
    else:
        print("YES")
