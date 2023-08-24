import math

n = int(input())
a = map(int, input().split())
arr = sorted(a)
ok = 0
for i in range(0, len(arr) - 1):
    if arr[i + 1] - arr[i] != 1:
        ok = 1
        print(arr[i] + 1) 
        break
if ok == 0:
    print(arr[-1] + 1)


