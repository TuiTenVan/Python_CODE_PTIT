def tich(n):
    tich = 1
    while n > 0:
        tich *= n % 10
        n //= 10
    return tich
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if tich(arr[i]) > tich(arr[j]):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            elif tich(arr[j]) == tich(arr[i]) and arr[j] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    for i in arr:
        print(i, end=" ")
    print()

