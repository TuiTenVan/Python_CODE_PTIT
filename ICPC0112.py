import math

def snt(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    x = int(input())
    count = 0
    for j in range(2, x - 1):
        if (snt(j) and snt(j + 2) and snt(j + 6)) or (snt(j) and snt(j + 4) and snt(j + 6)):
            if(j + 6 < x):
                count += 1
    print(count)