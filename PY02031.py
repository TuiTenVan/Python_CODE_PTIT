import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n, m = map(int, input().split())
matrix = []
for _ in range(0, n):
    row = list(map(int, input().split()))
    matrix.append(row)
for  i in range(n):
    for j in range(m):
        if snt(matrix[i][j]):
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end= " ")
    print()
    