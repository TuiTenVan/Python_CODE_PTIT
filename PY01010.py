t = int(input())
for i in range(t):
    x = input()
    s1 = x[:2]
    s2 = x[-2:]
    # print(int(s1))
    # print(int(s2))
    if int(s1) == int(s2):
        print("YES")
    else:
        print("NO")
