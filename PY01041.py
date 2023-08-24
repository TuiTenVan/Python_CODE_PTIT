def giam(s):
    for i in range(0, len(s) - 1):
        if int(s[i]) <= int(s[i + 1]):
            return False
    return True

t = int(input())  # Đọc số bộ test
for _ in range(t):
    s = input()  # Đọc chuỗi s
    i = 0
    ok = 0
    while i <= len(s) - 1:
        if i < len(s) - 1 and int(s[i]) < int(s[i + 1]):
            i += 1
        else:
            if giam(s[i:]) == False:
                ok = 1
                break
            i += 1
    if ok == 0 and len(s) >= 3:
        print("YES")
    else:
        print("NO")
