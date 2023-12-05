from itertools import *

t = int(input())
for _ in range(t):
    n = int(input())
    arr = permutations([x for x in range(1, n + 1)])
    a = list(arr)
    a.sort(reverse=True)
    print(len(a))
    for j in a:
        for x in j:
            print(x, end="")
        print(end=" ")
    print()