t = int(input())
for j in range(t):
    s1 = input()
    s2 = input()
    a1 = []
    a2 = []
    for i in range(len(s1)):
        a1.append(s1[i])
    for i in range(len(s2)):
        a2.append(s2[i])
    a1.sort()
    a2.sort()
    print("Test " + str(j + 1) + ": ", end="")
    if(a1 == a2):
        print("YES")
    else:
        print("NO")
    