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
    cnt = 0
    for j in s:
        if snt(int(j)):
            cnt += 1
    if snt(len(s)) and cnt >= len(s) - cnt:
        print("YES")
    else:
        print("NO")

