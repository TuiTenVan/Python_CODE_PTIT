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
    cnt = 0
    for j in range(0, len(s)):
        if snt(int(s[j])):
            cnt += 1
    if snt(len(s)) and cnt >= len(s) - cnt:
        print("YES")
    else:
        print("NO")
