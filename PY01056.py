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
    s = input()
    ok = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            if int(s[i]) % 2 != 0:
                ok = 1
                break
        else:
            if int(s[i]) % 2 == 0:
                ok = 1
                break
    sum = 0
    for i in s:
        sum += int(i)
    if(ok == 0 and snt(sum)):
        print("YES")
    else:
        print("NO")
