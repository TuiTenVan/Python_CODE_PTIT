
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    ans = [0] * len(a)
    for i in range(n):
        while arr and a[i] >= a[arr[-1]]:
            arr.pop()
        if not arr:
            print(i + 1, end=" ")
        else:
            print(i - arr[-1], end=" ")
        arr.append(i)
    print()