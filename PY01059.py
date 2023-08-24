t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    tich = 1
    ok = 1
    for k in range(0, len(s)):
        if k % 2 != 0:
            sum += int(s[k])
        else:
            if int(s[k]) != 0:
                tich *= int(s[k])
                ok = 0
    if(ok == 1):
        tich = 0
    print(tich, sum)