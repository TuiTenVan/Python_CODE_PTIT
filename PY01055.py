t = int(input())
for _ in range(t):
    s = input()
    ok = 0
    for i in range(0, len(s) - 2, 2):
        if int(s[i]) != int(s[i + 2]):
            ok = 1
            break
    if ok == 1 or len(s) % 2 == 0 or str(s[0]) == str(s[1]):
        print("NO")
    else:
        print("YES")