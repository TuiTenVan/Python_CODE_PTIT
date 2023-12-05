n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr1 = set(a)
arr2 = set(b)
if arr1 == arr2:
    print("YES")
else:
    print("NO")