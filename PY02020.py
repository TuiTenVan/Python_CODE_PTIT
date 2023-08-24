n = int(input())
a = list(map(float, input().split()))
arr = sorted(a)
sum = 0
cnt = 0
for i in arr:
    if i != arr[0] and i != arr[n - 1]:
        sum += i
        cnt += 1
x = sum / cnt
print('{:.2f}'.format(x))
