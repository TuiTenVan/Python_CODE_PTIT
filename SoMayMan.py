from math import *

if __name__=='__main__':
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    max_value=-10**9
    min_value=10**9
    for i in range(n):
        for j in range(m):
            if a[i][j] >max_value:
                max_value=a[i][j]
    for i in range(n):
        for j in range(m):
            if a[i][j] < min_value:
                min_value=a[i][j]
    res=max_value-min_value
    cnt=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==res:
                cnt+=1
    if cnt==0:
        print('NOT FOUND')
    else:
        print(res)
        for i in range(n):
            for j in range(m):
                if a[i][j]==res:
                    print('Vi tri ','[',i,']','[',j,']',sep='')