import math
n = int(input())
a = list(map(int, input().split()))
arr = sorted(a)
x = arr[0] * arr[1]
k = arr[0] * arr[1] * arr[-1]
y = arr[-1] * arr[-2]
z = arr[-1] * arr[-2] * arr[-3]
print(max(x, max(max(y, z), k)))