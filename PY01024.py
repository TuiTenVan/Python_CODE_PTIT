import math
t = int(input())
for _ in range(t):
    s = input()
    sum1 = 0
    for i in range(len(s)):
        sum1 += int(s[i]) - int('0')
    ok = 0
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            ok = 1
            break
    if ok == 0 and sum1 % 10 == 0:
        print("YES")
    else:
        print("NO")