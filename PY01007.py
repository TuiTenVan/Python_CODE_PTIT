t = int(input())
for i in range(t):
    n, x, m = map(float, input().split())
    sum = 0
    cnt = 0
    while sum < m:
        sum = (n + n * x / 100)
        cnt += 1
        n = sum
    print(cnt)