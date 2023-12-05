t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    arr = set(a)
    list = []
    Min = min(a)
    Max = max(a)
    Len = Max - Min + 1
    print(Len - len(arr))