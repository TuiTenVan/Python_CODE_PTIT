t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    kernel = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    for i in range(3):
        row = list(map(int, input().split()))
        kernel.append(row)
    ans = 0
    for i in range(n - 2):
        for j in range(m - 2):
            s = 0
            for k in range(3):
                for l in range(3):
                    s += int(kernel[k][l]) * int(matrix[i + k][j + l])
            ans += s
    print(ans)    
