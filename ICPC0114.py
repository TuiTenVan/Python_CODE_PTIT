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
    if(snt(dao)):
        return True
    else:
        return False
def sum(x):
    sum = 0
    while x > 0:
        r = x % 10
        if(snt(r) == False):
            return False
        sum += r
        x //= 10
    if(snt(sum) == True):
        return True
    else:
        return False
t = int(input())
for i in range(t):
    x = int(input())
    if(snt(x) and check(x) and sum(x)):
        print("Yes")
    else:
        print("No")