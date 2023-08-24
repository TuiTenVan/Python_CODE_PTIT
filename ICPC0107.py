
T = int(input())
for _ in range(T):
    m, n = input().split()
    X1 = input().strip()
    if(X1.count(' ')):
        X1, X2 = X1.split()
    else:
        X2 = input()
    p = min(m, n)
    q = max(m, n)
    ans_min = int(X1.replace(q, p)) + int(X2.replace(q, p))
    ans_max = int(X1.replace(p, q)) + int(X2.replace(p, q))
    print(ans_min, end=" ")
    print(ans_max)