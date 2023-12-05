t = int(input())
for _ in range(t):
    n, m, k = [int(x) for x in input().split()]
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
    a3 = [int(x) for x in input().split()]
    ans = []
    p1, p2, p3 = 0, 0, 0
    while p1 < n and p2 < m and p3 < k:
        if a1[p1] == a2[p2] and a2[p2] == a3[p3]:
            ans.append(a1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif a1[p1] < a2[p2]: p1 += 1
        elif a2[p2] < a3[p3]: p2 += 1
        elif a1[p1] > a3[p3]: p3 += 1
    if len(ans) == 0: 
        print("NO")
    else:
        ans.sort(key=lambda x : x)
        for i in ans:
            print(i, end=" ")
        print()