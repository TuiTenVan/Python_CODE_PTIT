t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    ok = 1
    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[n - i]) - ord(s[n - i - 1])):
            ok = 0
            break
    if ok == 0:
        print("NO")
    else:
        print("YES")
