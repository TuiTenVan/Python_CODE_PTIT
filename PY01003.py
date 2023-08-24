import math
t = int(input())
for i in range(t):
    x = int(input())
    if(x <= 10):
        print(x)
    elif x > 5 and x <= 10:
        print(10)
    else:
        cnt = 0
        while(x >= 10):
            r = x % 10
            x //= 10
            if r >= 5:
                x += 1
            cnt += 1
        x = x * pow(10, cnt)
        print(x)