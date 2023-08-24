t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    values = map(int, input().split())
    arr = []
    a = []
    for value in values:
        arr.append(value)
    x = arr[d:] + arr[:d]
    print(' '.join(map(str, x)))