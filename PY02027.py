t = int(input())
list = []
for _ in range(t):
    s = input()
    s += "@"
    tmp = ""
    for j in range(len(s)):
        if s[j] >= '0' and s[j] <= '9':
            tmp += s[j]
        else:
            if tmp != "":
                list.append(int(tmp))
            tmp = ""
list.sort(key=lambda x: x)
for i in list:
    print(i)