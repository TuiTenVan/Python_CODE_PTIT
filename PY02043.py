t = int(input())
for _ in range(t):
    s = input()
    x = input()
    i = 0
    cnt = 0
    while i <= len(s) - len(x):
        if s[i:i + len(x)] == x:
            cnt += 1
            i += len(x)
        else:
            i += 1
    print(cnt)
