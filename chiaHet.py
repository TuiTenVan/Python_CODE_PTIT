t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if(a % b == 0 or b % a == 0):
        print("YES")
    else:
        print("NO")
