t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    if n % 2 != 0:
        for j in range(1, n + 1):
            if(j % 2 != 0):
                sum += 1 / j
    else:
        for j in range(1, n + 1):
            if(j % 2 == 0):
                sum += 1 / j
    print(f"{sum:.6f}")