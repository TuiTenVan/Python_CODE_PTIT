def thuanNghich(n):
    dao = 0
    m = n
    while m > 0:
        dao = dao * 10 + m % 10
        m //= 10
    if dao == n:
        return True
    else:
        return False
t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if(thuanNghich(sum) and sum > 9):
        print("YES")
    else:
        print("NO")