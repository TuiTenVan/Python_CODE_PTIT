import math
t = int(input())
for k in range(t):
    s = input()
    x = ''.join(reversed(s))
    ok = 0
    for i in range(1, len(s)):
        if(abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(x[i]) - ord(x[i - 1]))):
            ok = 1
            break
    if ok == 1:
        print("NO")
    else:
        print("YES")