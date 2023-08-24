import math
def snt(n):
    if n < 2:
        return  False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
count = {}
for i in a:
    if snt(i):
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
for i in count:
    print(str(i) + " " + str(count[i]))
