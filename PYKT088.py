def check(n):
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if(j * j != i):
                    tmp += 2
                else:
                    tmp += 1
        if tmp == 9:
            cnt += 1
    return cnt
n = int(input())
print(check(n))
