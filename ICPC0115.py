import math
t = int(input())
for i in range(0, t):
    x = int(input())
    y = x
    sum = 0
    while x > 0:
        r = x % 10
        sum += math.factorial(r)
        x //= 10
    if(sum == y):
        print("Yes")
    else:
        print("No")