t = int(input()) 
for _ in range(t):
    s = input() 
    k = input()  
    cnt = 0
    i = 0
    while i <= len(s) - len(k): 
        if s[i:i+len(k)] == k:  
            cnt += 1
            i += len(k)  
        else:
            i += 1
    print(cnt)
