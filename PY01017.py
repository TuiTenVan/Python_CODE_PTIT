t = int(input())
for i in range(t):
    s = input()
    res = ""
    cnt = 1
    for j in range(1, len(s)):
        if s[j] == s[j - 1]:
            cnt += 1
        else:
            res += str(cnt) + s[j - 1]
            cnt = 1
    res += str(cnt) + s[-1]
    print(res)