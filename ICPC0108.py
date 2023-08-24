t = int(input())
for _ in range(t):
    a = int(input())
    arr = []
    values = input().split()
    for value in values:
        x = int(value)
        arr.append(x)
    arr.sort()
    cnt = 0
    for i in range(a - 2):
        left, right = i + 1, a - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] == 0:
                cnt += 1
                left += 1
            elif arr[i] + arr[left] + arr[right] < 0:
                left += 1
            else:
                right -= 1
    
    print(cnt)
