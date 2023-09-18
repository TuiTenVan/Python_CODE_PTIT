n = int(input())
matrix = []
for i in range(n):
    row = input()
    matrix.append(row)
count = 0
for i in range(n):
    res = 0
    for j in range(n):
        if matrix[i][j] == 'C':
            res += 1
    count += res * (res - 1) // 2
for i in range(n):
    res = 0
    for j in range(n):
        if matrix[j][i] == 'C':
            res += 1
    count += res * (res - 1) // 2
print(count)
