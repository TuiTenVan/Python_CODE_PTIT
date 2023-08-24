t = int(input())
for i in range(t):
    s = input()
    tich = 1
    for j in s:
        if int(j) != 0:
            tich *= int(j)
    print(tich)