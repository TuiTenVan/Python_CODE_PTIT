t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")