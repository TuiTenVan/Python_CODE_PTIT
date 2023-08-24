t = int(input())
for k in range(t):
    n = int(input())
    res = "1 * "
    for i in range(2, n):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            res += str(i) + "^" + str(cnt) + " * "
    if n > 1:
        res += str(n) + "^1"
        print(res)
    else:
        print(''.join(res[:-3]))