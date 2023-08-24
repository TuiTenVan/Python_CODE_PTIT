t = int(input()) 
for _ in range(t):
    a, b = map(int, input().split())  
    fibo = [0, 1, 1]
    for i in range(3, 93):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    for j in range(a, b + 1):
        print(fibo[j], end=" ")
    print()
