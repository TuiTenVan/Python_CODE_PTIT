import math
x = int(input())
if(x <= 10 and x > 0):
    print(x)
elif x == 0:
    print(1)
else:
    cnt = 0
    while(x >= 100):
        r = x % 10
        cnt += 1
        x //= 10
    k = x % 10
    x //= 10
    cnt += 1
    if k >= 5 :
        x = (x + 1) * pow(10, cnt)
    else:   
        x = x * pow(10, cnt)
    print(x)