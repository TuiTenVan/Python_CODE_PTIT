t = int(input())
for i in range(0, t):
    a = input()
    if int(a[-1]) == int(a[0]):
        print("YES")
    else:
        print("NO")