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
    sum = 0
    for j in s:
        sum += int(j)
    if snt(sum) == True:
        print("YES")
    else:
        print("NO")

