t=int(input())
for i in range(1,t+1):
    n=int(input())
    list=[]
    a=[int(x) for x in input().split()]
    max1=1000000000
    max2=1000000000
    max3=1000000000
    for j in range(1,n + 1):
        if(a[j]<max1):
            max3=max2
            max2=max1
            max1=a[j]
        elif(a[j]<max2):
            max3=max2
            max2=a[j]
        elif(a[j]<max3):
            max3=a[j]
    print(max1+max2+max3)