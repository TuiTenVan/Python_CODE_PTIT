import math

def snt(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
def check(x):
    m = x
    dao = 0
    while m > 0:
        dao = dao * 10 + m % 10
        m //= 10
    return dao
t = int(input())
for i in range(t):
    x = int(input())
    list = []
    for j in range(1, x):
        if(snt(j) and snt(check(j)) and check(j) != j):
            if(check(j) <= x):
                if j not in list:
                    list.append(j)
                    list.append(check(j))
    for k in list:
        print(k, end=' ')
    print()