if __name__ == "__main__":
    t = int(input())
    a = []
    for _ in range(t):
        n, m = map(int, input().split())
        matrix = []
        hoanvi = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            row = list(map(int, input().split()))
            matrix.append(row) 
        for i in range(m) :
            for j in range(n):
                hoanvi[i][j] = matrix[j][i]
        c = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    c[i][j] += matrix[i][k] * hoanvi[k][j]
        for i in range(n):
            for j in range(n):
                print(c[i][j], end=" ")
            print()
        print()