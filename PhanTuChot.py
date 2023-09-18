def left(a, x):
    for i in range(x):
        if(a[i] >= a[x]):
            return False
    return True
def right(a, x):
    for i in range(x, len(a)):
        if(a[i] < a[x]):
            return False
    return True
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = set()
    for i in range(n):
        if left(a, i):
            if right(a, i):
                ans.add(a[i])
    print(len(ans))

