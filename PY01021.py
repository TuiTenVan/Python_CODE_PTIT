t = int(input())
for _ in range(t):
    s = input()
    list = []
    ans = 0
    for i in range(len(s)):
        if not s[i].isdigit():
            list.append(s[i])
        else:
            ans += int(s[i])
    list.sort()
    for i in list:
        print(i, end="")
    print(ans)