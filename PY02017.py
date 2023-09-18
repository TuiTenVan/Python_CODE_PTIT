from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)
    for i in a:
        if(counter[i] % 2 != 0):
            print(i)
            break