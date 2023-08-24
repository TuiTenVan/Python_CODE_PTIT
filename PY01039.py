t = int(input())
for i in range(t):
    s = input()
    a = set()
    ok = 0
    for j in s:
        a.add(j)
    for j in range(2, len(s)):
        if int(s[j]) != int(s[j - 2]):
            ok = 1
            break
    if ok == 1 or len(a) != 2:
        print("NO")
    else:
        print("YES")
    