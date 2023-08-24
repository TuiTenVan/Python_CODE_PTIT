t = int(input())
for i in range(t):
    n = int(input())
    a = map(int, input().split())
    ans = {}
    max_cnt = 0
    index = 0
    for j in a:
        if j in ans:
            ans[j] += 1
        else:
            ans[j] = 1
        if ans[j] > max_cnt:
            max_cnt = ans[j] 
            index = j
    if max_cnt > n // 2:
        print(index)
    else:
        print("NO")
    